<script lang="ts">
  import { page } from '$app/state';
  import { project } from '$lib/project.svelte.ts';
</script>

<div class="middle-column">
    <h1>{project.getThemeById(Number(page.params.slug))?.title}</h1>
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
</style>