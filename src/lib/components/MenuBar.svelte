<script lang="ts">
    import { projectStore } from "$lib/stores/project.svelte";

    type SeparatorItem = { separator: true };
    type ActionItem = { label: string; shortcut?: string; action: () => void };
    type MenuEntry = ActionItem | SeparatorItem;

    type Menu = {
        id: string;
        label: string;
        items: MenuEntry[];
    };

    const menus: Menu[] = [
        // Ideas for future implementation are commented out for now

        {
            id: "file",
            label: "File",
            items: [
                {
                    label: "New Project",
                    shortcut: "Ctrl+N",
                    action: () => projectStore.newProject(),
                },
                {
                    label: "Open Project...",
                    shortcut: "Ctrl+O",
                    action: () => projectStore.openProject(),
                },
                {
                    label: "Save Project",
                    shortcut: "Ctrl+S",
                    action: () => projectStore.saveProject(),
                },
                {
                    label: "Close Project...",
                    shortcut: "",
                    action: () => projectStore.closeProject(),
                },
                //{ separator: true },
                //{ label: 'Import Files...', action: () => {} },
                //{ label: 'Export Project...', action: () => {} },
                //{ separator: true },
                //{ label: 'Project Properties...', action: () => {} },
                //{ separator: true },
                //{ label: 'Exit', shortcut: 'Alt+F4', action: () => {} },
            ],
        },
        {
            id: "edit",
            label: "Edit",
            items: [
                //{ label: 'Undo', shortcut: 'Ctrl+Z', action: () => {} },
                //{ label: 'Redo', shortcut: 'Ctrl+Y', action: () => {} },
            ],
        },
        {
            id: "view",
            label: "View",
            items: [
                // { label: 'Toggle Sidebar', shortcut: 'Ctrl+B', action: () => {} },
                // { separator: true },
                // { label: 'Zoom In', shortcut: 'Ctrl++', action: () => {} },
                // { label: 'Zoom Out', shortcut: 'Ctrl+-', action: () => {} },
                // { label: 'Reset Zoom', shortcut: 'Ctrl+0', action: () => {} },
            ],
        },
        {
            id: "project",
            label: "Project",
            items: [
                // { label: 'Project Properties...', action: () => {} },
                // { separator: true },
                // { label: 'Classifications...', action: () => {} },
                // { label: 'Relationships...', action: () => {} },
            ],
        },
        {
            id: "analysis",
            label: "Analysis",
            items: [
                // { label: 'Text Search Query', action: () => {} },
                // { label: 'Coding Query', action: () => {} },
                // { separator: true },
                // { label: 'Word Frequency...', action: () => {} },
            ],
        },
        {
            id: "help",
            label: "Help",
            items: [
                // { label: 'Documentation', action: () => {} },
                // { label: 'Keyboard Shortcuts', action: () => {} },
                // { separator: true },
                // { label: 'About Scramble', action: () => {} },
            ],
        },
    ];

    let openMenu = $state<string | null>(null);

    function toggleMenu(id: string, e: MouseEvent) {
        e.stopPropagation();
        openMenu = openMenu === id ? null : id;
    }

    function closeMenus() {
        openMenu = null;
    }

    function handleItemClick(item: MenuEntry) {
        if (!("separator" in item)) {
            item.action();
            closeMenus();
        }
    }
</script>

<svelte:document onclick={closeMenus} />

<header class="menu-bar">
    {#each menus as menu}
        <div class="menu-item" class:open={openMenu === menu.id}>
            <button
                class="menu-trigger"
                onclick={(e) => toggleMenu(menu.id, e)}
            >
                {menu.label}
            </button>
            {#if openMenu === menu.id}
                <div
                    class="menu-dropdown"
                    role="menu"
                    tabindex="-1"
                    onclick={(e) => e.stopPropagation()}
                    onkeydown={(e) => e.stopPropagation()}
                >
                    {#each menu.items as item}
                        {#if "separator" in item}
                            <div class="menu-separator" role="separator"></div>
                        {:else}
                            <button
                                class="dropdown-item"
                                onclick={() => handleItemClick(item)}
                            >
                                <span class="item-label">{item.label}</span>
                                {#if item.shortcut}
                                    <span class="item-shortcut"
                                        >{item.shortcut}</span
                                    >
                                {/if}
                            </button>
                        {/if}
                    {/each}
                </div>
            {/if}
        </div>
    {/each}
</header>

<style>
    .menu-bar {
        display: flex;
        align-items: center;
        height: var(--menubar-height);
        background: var(--color-menubar-bg);
        border-bottom: 1px solid var(--color-border);
        padding: 0 4px;
        user-select: none;
        flex-shrink: 0;
    }

    .menu-item {
        position: relative;
    }

    .menu-trigger {
        all: unset;
        display: flex;
        align-items: center;
        height: var(--menubar-height);
        padding: 0 10px;
        font-size: 13px;
        color: var(--color-text);
        border-radius: 4px;
        cursor: default;
        transition: background 0.1s;
    }

    .menu-trigger:hover,
    .menu-item.open .menu-trigger {
        background: var(--color-surface-hover);
    }

    .menu-dropdown {
        position: absolute;
        top: calc(100% + 2px);
        left: 0;
        min-width: 220px;
        background: var(--color-surface);
        border: 1px solid var(--color-border);
        border-radius: 6px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
        padding: 4px;
        z-index: 1000;
    }

    .dropdown-item {
        all: unset;
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 100%;
        box-sizing: border-box;
        padding: 5px 10px;
        font-size: 13px;
        color: var(--color-text);
        border-radius: 4px;
        cursor: default;
        transition: background 0.1s;
    }

    .dropdown-item:hover {
        background: var(--color-accent-bg);
        color: var(--color-accent);
    }

    .item-shortcut {
        font-size: 11px;
        color: var(--color-text-muted);
        margin-left: 24px;
    }

    .dropdown-item:hover .item-shortcut {
        color: var(--color-accent);
        opacity: 0.75;
    }

    .menu-separator {
        height: 1px;
        background: var(--color-border);
        margin: 4px 6px;
    }
</style>
