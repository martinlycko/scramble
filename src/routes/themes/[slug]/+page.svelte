<script lang="ts">
  import { page } from '$app/state';
  import { project } from '$lib/project.svelte.ts';
  
  let displayThemeMenu = $state(false);
  let displayThemeRename = $state(false);

  let newThemeTitle = $state('');

  function toggleThemeMenu() {
    displayThemeMenu = !displayThemeMenu;
  }

  function toggleThemeRename() {
    displayThemeRename = !displayThemeRename;
  }

  function renameTheme() {
    if (newThemeTitle.trim() !== '') {
      project.renameThemeById(Number(page.params.slug), newThemeTitle.trim());
      newThemeTitle = '';
      displayThemeRename = false;
    }
  }
</script>

<div class="middle-column">
    <div class="header">
        <h1>{project.getThemeById(Number(page.params.slug))?.title}</h1>
        <div class="actions">
            <button class="icon" onclick={toggleThemeMenu}>⋮</button>
        </div>
    </div>
    {#if displayThemeMenu}
        <div>
            <button onclick={toggleThemeRename}>Rename</button>
            <button onclick={() => project.removeThemeById(Number(page.params.slug))}>Delete</button>
        </div>
    {/if}
    {#if displayThemeRename}
        <div>
            <input bind:value={newThemeTitle} placeholder="New Name" />
            <button onclick={() => renameTheme()}>Save</button>
            <button onclick={() => displayThemeRename = false}>Cancel</button>
        </div>
    {/if}
    {#each project.getCodedDocIDsForTheme(Number(page.params.slug)) as docID}
        <h3>{project.getDocumentById(docID)?.title}</h3>
        {#each project.getCodesByThemeAndDoc(Number(page.params.slug), docID) as code}
            <p>{code.content}</p>
        {/each}
    {/each}
</div>

<style>
    .middle-column{
        position: fixed;
        top: 0px;
        left: 20%;
        height: 100%;
        width: calc(60% - 50px);
        float: left;
        height: 100%;
    }

    h1 {
        margin: 0px;
        padding: 0px;
    }

    .header {
        display: flex;
        justify-content: space-between;
    }

    .actions {
        display: flex;
        align-self: right;
        margin: 5px;
    }

    .icon {
        font-size: 18px;
        background: #eee;
        border-radius: 4px;
        cursor: pointer;
    }
</style>