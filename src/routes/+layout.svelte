<script lang="ts">
  
	import favicon from '$lib/assets/svelte-logo.svg';
	import { page } from '$app/state';

	let { children } = $props();

  async function openProject() {  
    // Placeholder for open functionality
    console.log('💾 Opening save dialog...');
  }
  
  async function saveProject() {
    // Placeholder for save functionality
    console.log('Project saved.');
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