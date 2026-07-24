<script lang="ts">
    import { projectStore } from "$lib/stores/project.svelte";
    import { confirm } from "@tauri-apps/plugin-dialog";
    import SourceTree from "$lib/components/sources/SourceTree.svelte";
    import DocumentForm from "$lib/components/sources/DocumentForm.svelte";
    import DocumentView from "$lib/components/sources/DocumentView.svelte";

    let selectedId = $state<string | null>(null);
    let mode = $state<"view" | "new">("view");
    let newDocFolderId = $state<string | null>(null);

    let selectedDoc = $derived(
        selectedId
            ? (projectStore.sources.find((s) => s.id === selectedId) ?? null)
            : null,
    );

    function startNewDocument(folderId: string | null) {
        newDocFolderId = folderId;
        selectedId = null;
        mode = "new";
    }

    function selectDocument(id: string) {
        selectedId = id;
        mode = "view";
    }

    function saveNewDocument(title: string, content: string) {
        const doc = projectStore.addSource(title, content, newDocFolderId);
        selectedId = doc.id;
        mode = "view";
    }

    function cancelForm() {
        mode = "view";
    }

    async function deleteSelected() {
        if (!selectedId) return;
        const doc = projectStore.sources.find((s) => s.id === selectedId);
        const confirmed = await confirm(
            `Delete "${doc?.title ?? "this document"}"? This cannot be undone.`,
            { title: "Delete document", kind: "warning" },
        );
        if (!confirmed) return;
        projectStore.deleteSource(selectedId);
        selectedId = null;
        mode = "view";
    }

    function newRootFolder() {
        const name = prompt("Folder name")?.trim();
        if (name) projectStore.addFolder(name, null);
    }
</script>

<div class="sources-page">
    <aside class="sources-sidebar">
        <div class="sidebar-header">
            <h2>Sources</h2>
            <div class="header-actions">
                <button
                    class="icon-btn"
                    title="New folder"
                    onclick={newRootFolder}
                >
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>
                        <line x1="12" y1="11" x2="12" y2="16"/>
                        <line x1="9.5" y1="13.5" x2="14.5" y2="13.5"/>
                    </svg>
                </button>
                <button
                    class="icon-btn"
                    title="New document"
                    onclick={() => startNewDocument(null)}
                >
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                        <polyline points="14,2 14,8 20,8"/>
                        <line x1="12" y1="11" x2="12" y2="17"/>
                        <line x1="9" y1="14" x2="15" y2="14"/>
                    </svg>
                </button>
            </div>
        </div>
        <SourceTree
            {selectedId}
            onSelectDocument={selectDocument}
            onNewDocument={startNewDocument}
        />
    </aside>
    <main class="sources-main">
        {#if mode === "new"}
            {#key "new-" + (newDocFolderId ?? "root")}
                <DocumentForm onSave={saveNewDocument} onCancel={cancelForm} />
            {/key}
        {:else if selectedDoc}
            <DocumentView doc={selectedDoc} onDelete={deleteSelected} />
        {:else}
            <div class="empty-state">
                <p>Select a document from the sidebar, or add a new one to get started.</p>
                <button class="btn-primary" onclick={() => startNewDocument(null)}>
                    Add document
                </button>
            </div>
        {/if}
    </main>
</div>

<style>
    .sources-page {
        display: flex;
        height: 100%;
    }

    .sources-sidebar {
        width: var(--sidebar-width);
        flex-shrink: 0;
        display: flex;
        flex-direction: column;
        border-right: 1px solid var(--color-border);
        background: var(--color-sidebar-bg);
        overflow: hidden;
    }

    .sidebar-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 12px;
        border-bottom: 1px solid var(--color-border);
        flex-shrink: 0;
    }

    .sidebar-header h2 {
        margin: 0;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        color: var(--color-text-muted);
    }

    .header-actions {
        display: flex;
        gap: 2px;
    }

    .icon-btn {
        all: unset;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        border-radius: 5px;
        color: var(--color-text-muted);
        cursor: default;
    }

    .icon-btn:hover {
        background: var(--color-surface-hover);
        color: var(--color-text);
    }

    .sources-main {
        flex: 1;
        overflow: hidden;
        background: var(--color-surface);
    }

    .empty-state {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 14px;
        height: 100%;
        padding: 20px;
        text-align: center;
        color: var(--color-text-muted);
        font-size: 14px;
    }

    .empty-state p {
        margin: 0;
        max-width: 320px;
        line-height: 1.5;
    }

    .btn-primary {
        padding: 7px 16px;
        font-size: 13px;
        font-weight: 500;
        border-radius: 6px;
        border: none;
        cursor: pointer;
        background: var(--color-accent);
        color: #fff;
        font-family: inherit;
        transition: opacity 0.1s;
    }

    .btn-primary:hover {
        opacity: 0.85;
    }
</style>
