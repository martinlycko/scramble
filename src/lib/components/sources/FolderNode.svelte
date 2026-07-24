<script lang="ts">
    import { projectStore, type SourceFolder } from "$lib/stores/project.svelte";
    import { confirm } from "@tauri-apps/plugin-dialog";
    import DocumentRow from "./DocumentRow.svelte";
    import FolderNode from "./FolderNode.svelte";

    let {
        folder,
        depth,
        selectedId,
        onSelectDocument,
        onNewDocument,
    }: {
        folder: SourceFolder;
        depth: number;
        selectedId: string | null;
        onSelectDocument: (id: string) => void;
        onNewDocument: (folderId: string | null) => void;
    } = $props();

    let expanded = $state(true);

    let childFolders = $derived(
        projectStore.folders.filter((f) => f.parentId === folder.id),
    );
    let childDocuments = $derived(
        projectStore.sources.filter((s) => s.folderId === folder.id),
    );

    function toggle() {
        expanded = !expanded;
    }

    function rename(e: MouseEvent) {
        e.stopPropagation();
        const name = prompt("Rename folder", folder.name)?.trim();
        if (name) projectStore.renameFolder(folder.id, name);
    }

    function newSubfolder(e: MouseEvent) {
        e.stopPropagation();
        const name = prompt("New folder name")?.trim();
        if (name) projectStore.addFolder(name, folder.id);
        expanded = true;
    }

    function newDocument(e: MouseEvent) {
        e.stopPropagation();
        onNewDocument(folder.id);
    }

    async function remove(e: MouseEvent) {
        e.stopPropagation();
        const confirmed = await confirm(
            `Delete folder "${folder.name}" and everything inside it? This cannot be undone.`,
            { title: "Delete folder", kind: "warning" },
        );
        if (confirmed) {
            projectStore.deleteFolder(folder.id);
        }
    }
</script>

<div
    class="row folder-row"
    style={`padding-left: ${12 + depth * 16}px`}
    onclick={toggle}
    ondblclick={rename}
    role="button"
    tabindex="0"
    onkeydown={(e) => e.key === "Enter" && toggle()}
>
    <span class="chevron" class:expanded>
        <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9,18 15,12 9,6"/>
        </svg>
    </span>
    <span class="row-icon">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>
        </svg>
    </span>
    <span class="row-label" title={folder.name}>{folder.name}</span>
    <div class="row-actions">
        <button class="row-action" title="New document" onclick={newDocument}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14,2 14,8 20,8"/>
                <line x1="12" y1="11" x2="12" y2="17"/>
                <line x1="9" y1="14" x2="15" y2="14"/>
            </svg>
        </button>
        <button class="row-action" title="New subfolder" onclick={newSubfolder}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>
                <line x1="12" y1="11" x2="12" y2="16"/>
                <line x1="9.5" y1="13.5" x2="14.5" y2="13.5"/>
            </svg>
        </button>
        <button class="row-action" title="Delete folder" onclick={remove}>
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="3,6 5,6 21,6"/>
                <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
            </svg>
        </button>
    </div>
</div>

{#if expanded}
    {#each childFolders as child (child.id)}
        <FolderNode
            folder={child}
            depth={depth + 1}
            {selectedId}
            {onSelectDocument}
            {onNewDocument}
        />
    {/each}
    {#each childDocuments as doc (doc.id)}
        <DocumentRow
            {doc}
            depth={depth + 1}
            selected={selectedId === doc.id}
            onSelect={() => onSelectDocument(doc.id)}
        />
    {/each}
{/if}

<style>
    .row {
        display: flex;
        align-items: center;
        gap: 6px;
        padding-right: 8px;
        height: 28px;
        border-radius: 5px;
        cursor: default;
        color: var(--color-text);
        font-size: 12.5px;
        user-select: none;
    }

    .row:hover {
        background: var(--color-surface-hover);
    }

    .chevron {
        display: flex;
        flex-shrink: 0;
        transition: transform 0.1s;
        opacity: 0.7;
    }

    .chevron.expanded {
        transform: rotate(90deg);
    }

    .row-icon {
        display: flex;
        flex-shrink: 0;
        opacity: 0.8;
    }

    .row-label {
        flex: 1;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        font-weight: 500;
    }

    .row-actions {
        display: none;
        align-items: center;
        gap: 2px;
        flex-shrink: 0;
    }

    .row:hover .row-actions {
        display: flex;
    }

    .row-action {
        all: unset;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 20px;
        height: 20px;
        border-radius: 4px;
        color: var(--color-text-muted);
        cursor: default;
    }

    .row-action:hover {
        background: var(--color-border);
        color: var(--color-text);
    }
</style>
