<script lang="ts">
    let {
        projectName = null,
        sourceCount = 0,
        codeCount = 0,
        lastSaved = null,
    }: {
        projectName?: string | null;
        sourceCount?: number;
        codeCount?: number;
        lastSaved?: Date | null;
    } = $props();

    let lastSavedLabel = $derived(
        lastSaved
            ? lastSaved.toLocaleTimeString(undefined, {
                  hour: "2-digit",
                  minute: "2-digit",
              })
            : "Not saved",
    );
</script>

<footer class="status-bar">
    <div class="status-segment project-name">
        <svg
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
        >
            <path
                d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"
            />
        </svg>
        <span
            >{#if projectName}{projectName}{:else}No project open{/if}</span
        >
    </div>

    <div class="status-divider"></div>

    <div class="status-segment">
        <svg
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
        >
            <path
                d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
            />
            <polyline points="14,2 14,8 20,8" />
        </svg>
        <span>{sourceCount} {sourceCount === 1 ? "source" : "sources"}</span>
    </div>

    <div class="status-divider"></div>

    <div class="status-segment">
        <svg
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
        >
            <path
                d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"
            />
            <line x1="7" y1="7" x2="7.01" y2="7" />
        </svg>
        <span>{codeCount} {codeCount === 1 ? "code" : "codes"}</span>
    </div>

    <div class="status-spacer"></div>

    <div class="status-segment">
        <svg
            width="12"
            height="12"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
        >
            <circle cx="12" cy="12" r="10" />
            <polyline points="12,6 12,12 16,14" />
        </svg>
        <span
            >{#if lastSavedLabel != "Not saved"}Saved
            {/if}{lastSavedLabel}</span
        >
    </div>
</footer>

<style>
    .status-bar {
        display: flex;
        align-items: center;
        height: var(--statusbar-height);
        background: var(--color-menubar-bg);
        border-top: 1px solid var(--color-border);
        padding: 0 10px;
        flex-shrink: 0;
        overflow: hidden;
    }

    .status-segment {
        display: flex;
        align-items: center;
        gap: 5px;
        font-size: 11px;
        color: var(--color-text-muted);
        white-space: nowrap;
        padding: 0 4px;
    }

    .status-segment svg {
        flex-shrink: 0;
        opacity: 0.7;
    }

    .project-name {
        font-weight: 500;
        color: var(--color-text);
    }

    .project-name svg {
        opacity: 1;
    }

    .status-divider {
        width: 1px;
        height: 12px;
        background: var(--color-border);
        margin: 0 6px;
        flex-shrink: 0;
    }

    .status-spacer {
        flex: 1;
    }
</style>
