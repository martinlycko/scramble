<script lang="ts">
  import { page } from '$app/state';
  import { project } from '$lib/project.svelte.ts';

  let displayDocMenu = $state(false);
  let displayDocRename = $state(false);
  let displayRightMenu = $state("Themes");
  let displayAddTheme = $state(false);
  let displayAddAttribute = $state(false);

  let newDocTitle = $state('');
  let newThemeTitle = $state('');
  let newAttributeTitle = $state('');

  function toggleDocMenu() {
    displayDocMenu = !displayDocMenu;
  }

  function toggleDocRename() {
    displayDocRename = !displayDocRename;
  }

  function toggleAddTheme() {
    displayAddTheme = !displayAddTheme;
  }

  function toggleAddAttribute() {
    displayAddAttribute = !displayAddAttribute;
  }

  function toggleRightMenu() {
    if (displayRightMenu==="Themes") {
        displayRightMenu="Attributes"
    } else {
        displayRightMenu="Themes"
    }
  }

  function codeSelection(themeId: Number) {
    const selection = window.getSelection();
    const text = selection.toString();
    if (!text  || selection.rangeCount === 0) {
        console.log('No text selected.');
        return;
    }

    const range = selection.getRangeAt(0);
    const preRange = document.createRange();

    // Clone range to measure text before selection
    preRange.selectNodeContents(document.getElementById("document-container"));
    preRange.setEnd(range.startContainer, range.startOffset);
    const start = preRange.toString().length;
    const length = range.toString().length;
    const end = start + length;

    project.addCode(Number(page.params.slug),
                    themeId,
                    text,
                    start,
                    end,
                    length);
    }

  function renameDocument() {
    if (newDocTitle.trim() !== '') {
      project.renameDocumentById(Number(page.params.slug), newDocTitle.trim());
      newDocTitle = '';
      displayDocRename = false;
    }
  }
</script>

<div class="middle-column">
    <div class="header">
        <h1>{project.getDocumentById(Number(page.params.slug))?.title}</h1>
        <div class="actions">
            <button class="icon" onclick={toggleDocMenu}>⋮</button>
        </div>
    </div>
    {#if displayDocMenu}
        <div>
            <button onclick={toggleDocRename}>Rename</button>
            <button onclick={() => project.removeDocumentById(Number(page.params.slug))}>Delete</button>
        </div>
    {/if}
    {#if displayDocRename}
        <div>
            <input bind:value={newDocTitle} placeholder="New Title" />
            <button onclick={() => renameDocument()}>Save</button>
            <button onclick={() => displayDocRename = false}>Cancel</button>
        </div>
    {/if}
    <div id="document-container">{@html project.getDocumentById(Number(page.params.slug))?.content}</div>
</div>

<div class="right-column">
    {#if displayRightMenu==="Themes"}
        <div class="row">
            <h3 class="row-item">Themes</h3>
            <div class="row-item right-button">
                <button onclick={toggleAddTheme}>+</button>
                <button onclick={toggleRightMenu}>C</button>
            </div>    
        </div>
        {#if displayAddTheme}
            <input bind:value={newThemeTitle} placeholder="Theme Title" />
            <button onclick={() => { project.addTheme(newThemeTitle); newThemeTitle = ''; displayAddTheme = false; }}>Add</button>
        {/if}
        <div class="scrollable">
            {#each project.themes as theme}
                <button onclick={() => codeSelection(theme.id)}>"{theme.title}"</button><br>
            {/each}
        </div>
    {/if}
    {#if displayRightMenu==="Attributes"}
        <div class="row">
            <h3 class="row-item">Attributes</h3>
            <div class="row-item right-button">
                <button onclick={toggleAddAttribute}>+</button>
                <button onclick={toggleRightMenu}>C</button>
            </div>    
        </div>
        {#if displayAddAttribute}
            <input bind:value={newAttributeTitle} placeholder="Attribute Name" />
            <button onclick={() => { project.addAttribute(newAttributeTitle); newAttributeTitle = ''; displayAddAttribute = false; }}>Add</button>
        {/if}
        <div class="scrollable">
            {#each Array.from(project.getDocumentById(Number(page.params.slug))?.attributes.entries()) as [key, value]}
                <p>{key}: {value}</p>
            {/each}
        </div>
    {/if}
</div>

<style>
    .middle-column{
        position: fixed;
        top: 0px;
        left: 20%;
        height: 100%;
        width: calc(60% - 5px);
        float: left;
        height: 100%;
    }

    h1 {
        margin: 0px;
        padding: 0px;
    }

    .right-column{
        float: left;
        height: 100%;
        left: 80%;
        width: 20%;
        background-color:#aaa;
        position: fixed;
    }

    .row {
        display:table;
        background-color:#981111;
        width: 100%;
    }

    .row-item {
        display:table-cell;
    }

    .right-button {
        text-align: right;
    }

    .scrollable {
        height: calc(100% - 40px);
        overflow-y: auto;
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