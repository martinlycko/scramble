<script lang="ts">
  import { project } from '$lib/project.svelte.js';

  let title = $state('');
  let text = $state('');

  function addDocument() {
    project.documents.push({
        id: 1 + Math.max(0, ...project.documents.map(d => d.id)),
        title: title,
        content: text
    })
  }
</script>

<div class="middle-column">
    <input bind:value={title} placeholder="Document Title" />
    <textarea bind:value={text} placeholder="Document Text"></textarea>
    <button onclick="{addDocument}">Add Document</button>
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

    input {
        display: block;
        width: 100%;
        margin: 20px auto 10px auto;
        padding: 10px;
        font-size: 1.2em;
    }

    textarea {
        display: block;
        width: 100%;
        height: calc(100% - 150px);
        margin: 10px auto;
        padding: 10px;
        font-size: 1em;
        resize: none;
    }
</style>