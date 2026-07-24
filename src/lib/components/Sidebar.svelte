<script lang="ts">
    type NavSection = {
        id: string;
        label: string;
        icon: string;
    };

    const sections: NavSection[] = [
        {
            id: "sources",
            label: "Sources",
            icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14,2 14,8 20,8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
        <polyline points="10,9 9,9 8,9"/>
      </svg>`,
        },
        {
            id: "codes",
            label: "Codes",
            icon: `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/>
        <line x1="7" y1="7" x2="7.01" y2="7"/>
      </svg>`,
        },
    ];

    let { activeSection = $bindable("sources") }: { activeSection?: string } =
        $props();
</script>

<nav class="sidebar">
    <div class="sidebar-section">
        {#each sections as section}
            <button
                class="nav-item"
                class:active={activeSection === section.id}
                onclick={() => (activeSection = section.id)}
                title={section.label}
            >
                <span class="nav-icon">{@html section.icon}</span>
            </button>
        {/each}
    </div>
</nav>

<style>
    .sidebar {
        width: 50px;
        background: var(--color-sidebar-bg);
        border-right: 1px solid var(--color-border);
        display: flex;
        flex-direction: column;
        overflow-y: auto;
        flex-shrink: 0;
    }

    .sidebar-section {
        padding: 8px 6px;
        display: flex;
        flex-direction: column;
        gap: 2px;
    }

    .nav-item {
        all: unset;
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 7px 10px;
        border-radius: 6px;
        font-size: 13px;
        color: var(--color-text-muted);
        cursor: default;
        transition:
            background 0.1s,
            color 0.1s;
    }

    .nav-item:hover {
        background: var(--color-surface-hover);
        color: var(--color-text);
    }

    .nav-item.active {
        background: var(--color-accent-bg);
        color: var(--color-accent);
        font-weight: 500;
    }

    .nav-icon {
        display: flex;
        align-items: center;
        flex-shrink: 0;
        opacity: 0.9;
    }
</style>
