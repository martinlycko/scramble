<script lang="ts">
  import { projectStore } from "$lib/stores/project.svelte";
</script>

<div class="home">
  {#if !projectStore.path}
    <div class="welcome">
      <h1>Welcome to Scramble</h1>
      <p>Your qualitative data analysis workspace. Open a project to get started.</p>
      <div class="actions">
        <button class="btn-primary" onclick={() => projectStore.newProject()}>New Project</button>
        <button class="btn-secondary" onclick={() => projectStore.openProject()}>Open Project...</button>
      </div>
      {#if projectStore.error}
        <p class="error">{projectStore.error}</p>
      {/if}
    </div>
  {:else}
    <div class="welcome">
      <h1>{projectStore.name}</h1>
      <p>Project loaded. Sources and codes are empty — add some to get started.</p>
    </div>
  {/if}
</div>

<style>
  .home {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: var(--color-text);
  }

  .welcome {
    text-align: center;
    max-width: 400px;
  }

  h1 {
    font-size: 24px;
    font-weight: 600;
    margin: 0 0 8px;
    color: var(--color-text);
  }

  p {
    font-size: 14px;
    color: var(--color-text-muted);
    margin: 0 0 28px;
    line-height: 1.5;
  }

  .actions {
    display: flex;
    gap: 10px;
    justify-content: center;
  }

  button {
    padding: 8px 18px;
    font-size: 13px;
    font-weight: 500;
    border-radius: 6px;
    border: none;
    cursor: pointer;
    transition: opacity 0.1s;
    font-family: inherit;
  }

  button:hover {
    opacity: 0.85;
  }

  .btn-primary {
    background: var(--color-accent);
    color: #fff;
  }

  .btn-secondary {
    background: var(--color-surface);
    color: var(--color-text);
    border: 1px solid var(--color-border);
  }

  .error {
    margin: 16px 0 0;
    font-size: 13px;
    color: #dc2626;
  }
</style>
