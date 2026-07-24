<script lang="ts">
  import { projectStore } from "$lib/stores/project.svelte";
  import { uiStore } from "$lib/stores/ui.svelte";
  import ProjectPage from "$lib/components/pages/ProjectPage.svelte";
  import SourcesPage from "$lib/components/pages/SourcesPage.svelte";
</script>

{#if !projectStore.path || uiStore.activeSection === "project"}
  <ProjectPage />
{:else if uiStore.activeSection === "sources"}
  <SourcesPage />
{:else if uiStore.activeSection === "codes"}
  <div class="placeholder">Codes — coming soon.</div>
{/if}

<style>
  .placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: var(--color-text-muted);
    font-size: 14px;
  }
</style>
