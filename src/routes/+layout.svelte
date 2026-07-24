<script lang="ts">
    import type { Snippet } from "svelte";
    import MenuBar from "$lib/components/MenuBar.svelte";
    import Sidebar from "$lib/components/Sidebar.svelte";
    import StatusBar from "$lib/components/StatusBar.svelte";
    import { projectStore } from "$lib/stores/project.svelte";
    import { uiStore } from "$lib/stores/ui.svelte";

    let { children }: { children: Snippet } = $props();

    $effect(() => {
        if (!projectStore.path) {
            uiStore.activeSection = "project";
        }
    });
</script>

<div class="app-shell">
    <MenuBar />
    <div class="workspace">
        <Sidebar
            bind:activeSection={uiStore.activeSection}
            projectActive={!!projectStore.path}
        />
        <main class="content-area">
            {@render children()}
        </main>
    </div>
    <StatusBar
        projectName={projectStore.name}
        sourceCount={projectStore.sourceCount}
        codeCount={projectStore.codeCount}
        lastSaved={projectStore.lastSaved}
    />
</div>

<style>
    :global(*, *::before, *::after) {
        box-sizing: border-box;
    }

    :global(body) {
        margin: 0;
        padding: 0;
        overflow: hidden;
        font-family:
            -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
            sans-serif;

        --menubar-height: 28px;
        --sidebar-width: 200px;
        --statusbar-height: 22px;

        --color-bg: #f0f2f5;
        --color-surface: #ffffff;
        --color-menubar-bg: #f6f7f9;
        --color-sidebar-bg: #f0f1f4;
        --color-surface-hover: #e8eaed;
        --color-border: #dde0e6;
        --color-text: #1c1e23;
        --color-text-muted: #6b7280;
        --color-accent: #2563eb;
        --color-accent-bg: #eff6ff;
    }

    @media (prefers-color-scheme: dark) {
        :global(body) {
            --color-bg: #1a1c20;
            --color-surface: #242629;
            --color-menubar-bg: #1e2024;
            --color-sidebar-bg: #1c1e22;
            --color-surface-hover: #2a2d32;
            --color-border: #333740;
            --color-text: #e8eaed;
            --color-text-muted: #9aa0aa;
            --color-accent: #3b82f6;
            --color-accent-bg: #1e3a5f;
        }
    }

    .app-shell {
        display: flex;
        flex-direction: column;
        height: 100vh;
        background: var(--color-bg);
        overflow: hidden;
    }

    .workspace {
        display: flex;
        flex: 1;
        overflow: hidden;
    }

    .content-area {
        flex: 1;
        overflow: auto;
        background: var(--color-bg);
    }
</style>
