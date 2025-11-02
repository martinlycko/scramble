<script lang="ts">
	import favicon from '$lib/assets/svelte-logo.svg';

	import { page } from '$app/state';
	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="sidenav">
  <a href="/documents" class:active={page.url.pathname === "/documents"}>Docs</a>
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