<script lang="ts">
    import type { SourceDocument } from "$lib/stores/project.svelte";

    let {
        doc,
        onDelete,
    }: {
        doc: SourceDocument;
        onDelete: () => void;
    } = $props();

    let createdLabel = $derived(
        new Date(doc.createdAt).toLocaleString(undefined, {
            dateStyle: "medium",
            timeStyle: "short",
        }),
    );
</script>

<div class="viewer">
    <div class="viewer-header">
        <div class="heading">
            <h2>{doc.title}</h2>
            <p class="meta">Added {createdLabel}</p>
        </div>
        <div class="actions">
            <button class="btn-danger" onclick={onDelete}>Delete</button>
        </div>
    </div>
    <div class="content">
        {#if doc.content.trim()}
            <p>{doc.content}</p>
        {:else}
            <p class="empty">This document has no text.</p>
        {/if}
    </div>
</div>

<style>
    .viewer {
        display: flex;
        flex-direction: column;
        height: 100%;
        padding: 20px 24px;
    }

    .viewer-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        gap: 16px;
        padding-bottom: 14px;
        border-bottom: 1px solid var(--color-border);
        flex-shrink: 0;
    }

    h2 {
        margin: 0 0 4px;
        font-size: 19px;
        font-weight: 600;
        color: var(--color-text);
        word-break: break-word;
    }

    .meta {
        margin: 0;
        font-size: 12px;
        color: var(--color-text-muted);
    }

    .actions {
        display: flex;
        gap: 8px;
        flex-shrink: 0;
    }

    button {
        padding: 6px 14px;
        font-size: 13px;
        font-weight: 500;
        border-radius: 6px;
        border: none;
        cursor: pointer;
        transition: opacity 0.1s;
        font-family: inherit;
        white-space: nowrap;
    }

    button:hover {
        opacity: 0.85;
    }

    .btn-danger {
        background: #fef2f2;
        color: #dc2626;
        border: 1px solid #fecaca;
    }

    .content {
        flex: 1;
        overflow-y: auto;
        padding-top: 16px;
    }

    .content p {
        margin: 0;
        font-size: 14px;
        line-height: 1.7;
        color: var(--color-text);
        white-space: pre-wrap;
        word-break: break-word;
    }

    .content .empty {
        color: var(--color-text-muted);
        font-style: italic;
    }
</style>
