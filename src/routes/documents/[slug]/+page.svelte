<script lang="ts">
  import { page } from '$app/state';
  import { project } from '$lib/project.svelte.ts';

  let displayAddTheme = $state(false);
  let newThemeTitle = $state('');

  function toggleAddTheme() {
    displayAddTheme = !displayAddTheme;
  }
</script>

<div class="middle-column">
    <h1>{project.getDocumentById(Number(page.params.slug))?.title}</h1>
    <div>{@html project.getDocumentById(Number(page.params.slug))?.content}</div>
</div>

<div class="right-column">
    <div class="row">
        <h3 class="row-item">Themes</h3>
        <div class="row-item right-button">
            <button onclick={toggleAddTheme}>+</button>
        </div>
    </div>
    {#if displayAddTheme}
        <input bind:value={newThemeTitle} placeholder="Theme Title" />
        <button onclick={() => { project.addTheme(newThemeTitle); newThemeTitle = ''; displayAddTheme = false; }}>Add</button>
    {/if}
    <div class="scrollable">
        {#each project.themes as theme}
            <li class="ColumnList">
                <a href="../../themes/{theme.id}">{theme.title}</a>
            </li>
        {/each}
    </div>
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

    .ColumnList {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        padding: 0px;
    }

    .scrollable {
        height: calc(100% - 40px);
        overflow-y: auto;
    }
</style>