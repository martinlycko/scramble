<script lang="ts">
    import { projectStore, type SourceDocument } from "$lib/stores/project.svelte";
    import { confirm } from "@tauri-apps/plugin-dialog";

    let {
        doc,
        depth,
        selected,
        onSelect,
    }: {
        doc: SourceDocument;
        depth: number;
        selected: boolean;
        onSelect: () => void;
    } = $props();

    async function remove(e: MouseEvent) {
        e.stopPropagation();
        const confirmed = await confirm(`Delete "${doc.title}"? This cannot be undone.`, {
            title: "Delete document",
            kind: "warning",
        });
        if (confirmed) {
            projectStore.deleteSource(doc.id);
        }
    }
</script>

<div
    class="row doc-row"
    class:selected
    style={`padding-left: ${12 + depth * 16}px`}
    onclick={onSelect}
    role="button"
    tabindex="0"
    onkeydown={(e) => e.key === "Enter" && onSelect()}
>
    <span class="row-icon">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14,2 14,8 20,8"/>
        </svg>
    </span>
    <span class="row-label" title={doc.title}>{doc.title || "Untitled"}</span>
    <button class="row-action" title="Delete document" onclick={remove}>
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="3,6 5,6 21,6"/>
            <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
        </svg>
    </button>
</div>

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

    .row.selected {
        background: var(--color-accent-bg);
        color: var(--color-accent);
    }

    .row-icon {
        display: flex;
        flex-shrink: 0;
        opacity: 0.75;
    }

    .row-label {
        flex: 1;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }

    .row-action {
        all: unset;
        display: none;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        width: 20px;
        height: 20px;
        border-radius: 4px;
        color: var(--color-text-muted);
        cursor: default;
    }

    .row:hover .row-action {
        display: flex;
    }

    .row-action:hover {
        background: var(--color-border);
        color: var(--color-text);
    }
</style>
