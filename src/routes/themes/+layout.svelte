<script lang="ts">
  import { project } from '$lib/project.svelte.ts';

  let { children } = $props();
</script>

<div>
  <div class="left-column">
    <div class="row">
        <h3 class="row-item">Themes</h3>
    </div>
    <div class="scrollable">
        <ul class="ColumnList">
            {#each project.themes as theme}
                <li class="ColumnListItem"><a href="/themes/{theme.id}">{theme.title}</a></li>
            {/each}
        </ul>
    </div>        
  </div>
</div>

{@render children?.()}

<style>
  .left-column{
        position: fixed;
        top: 0px;
        left: 50px;
        float: left;
        height: 100%;
        width: calc(20% - 50px);
        background-color:#aaa;
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

    .ColumnListItem {
        color: black;
        text-align: left;
        text-decoration: none;
    }

    .scrollable {
        height: calc(100% - 40px);
        overflow-y: auto;
    }
</style>