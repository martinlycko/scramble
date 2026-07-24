<script lang="ts">
    import { projectStore } from "$lib/stores/project.svelte";
    import FolderNode from "./FolderNode.svelte";
    import DocumentRow from "./DocumentRow.svelte";

    let {
        selectedId,
        onSelectDocument,
        onNewDocument,
    }: {
        selectedId: string | null;
        onSelectDocument: (id: string) => void;
        onNewDocument: (folderId: string | null) => void;
    } = $props();

    let rootFolders = $derived(
        projectStore.folders.filter((f) => f.parentId === null),
    );
    let rootDocuments = $derived(
        projectStore.sources.filter((s) => s.folderId === null),
    );
</script>

<div class="tree">
    {#each rootFolders as folder (folder.id)}
        <FolderNode {folder} depth={0} {selectedId} {onSelectDocument} {onNewDocument} />
    {/each}
    {#each rootDocuments as doc (doc.id)}
        <DocumentRow
            {doc}
            depth={0}
            selected={selectedId === doc.id}
            onSelect={() => onSelectDocument(doc.id)}
        />
    {/each}
    {#if rootFolders.length === 0 && rootDocuments.length === 0}
        <p class="empty-tree">No documents yet.</p>
    {/if}
</div>

<style>
    .tree {
        display: flex;
        flex-direction: column;
        gap: 1px;
        padding: 6px;
        overflow-y: auto;
        flex: 1;
    }

    .empty-tree {
        font-size: 12px;
        color: var(--color-text-muted);
        padding: 8px 6px;
        margin: 0;
        line-height: 1.5;
    }
</style>
