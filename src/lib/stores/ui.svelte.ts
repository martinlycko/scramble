export type Section = "sources" | "codes" | "project";

class UiStore {
    activeSection = $state<Section>("project");
}

export const uiStore = new UiStore();
