<script lang="ts">
  
	import favicon from '$lib/assets/svelte-logo.svg';
	import { page } from '$app/state';

  import { open, save } from '@tauri-apps/plugin-dialog';
  import { writeFile } from '@tauri-apps/plugin-fs';

  import { project } from '$lib/project.svelte.ts'

	let { children } = $props();

  async function openProject() {  
    const selected = await open({
      multiple: false,
      filters: [
        {
          name: "Scramble Project",
          extensions: ["scramble"]
        }
      ]
    });

    console.log("Selected file:", selected);
  }
  
  async function saveProject() {
    // Open Save dialog
    const filePath = await save({
      title: "Save Scramble Project",
      defaultPath: project.name + ".scramble",
      filters: [{ name: "Scramble Project", extensions: ["scramble"] }]
    });

    if (!filePath) return; // user cancelled

    const contents = JSON.stringify(project, null, 2);
    const bytes = new TextEncoder().encode(contents);

    // Write file
    await writeFile(filePath, bytes);
  }
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="sidenav">
  <button onclick={() => openProject() }>Open</button>
  <button onclick={() =>  saveProject() }>Save</button>
  <a href="/documents" class:active={page.url.pathname === "/documents"}>Docs</a>
  <a href="/themes" class:active={page.url.pathname === "/themes"}>Themes</a>
</div>

{@render children?.()}

<style>
  .sidenav {
    height: 100%;
    width: 50px;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: grey;
    overflow-x: hidden;
    padding-top: 3px;
  }

  .active {
	background-color: white;
  }
</style>