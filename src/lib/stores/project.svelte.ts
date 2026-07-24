import { save, open } from "@tauri-apps/plugin-dialog";
import { invoke } from "@tauri-apps/api/core";

type ProjectData = {
    name: string;
    created_at: string;
    sources: unknown[];
    codes: unknown[];
};

class ProjectStore {
    name = $state<string | null>(null);
    path = $state<string | null>(null);
    sourceCount = $state(0);
    codeCount = $state(0);
    lastSaved = $state<Date | null>(null);
    error = $state<string | null>(null);

    async newProject() {
        this.error = null;
        const path = await save({
            defaultPath: "Untitled.scramble",
            filters: [{ name: "Scramble Project", extensions: ["scramble"] }],
        });
        if (!path) return;

        const name = path.split(/[\\/]/).pop()!.replace(/\.scramble$/, "");
        try {
            const data = await invoke<ProjectData>("create_project", {
                path,
                name,
                createdAt: new Date().toISOString(),
            });
            this.apply(path, data);
        } catch (e) {
            this.error = String(e);
        }
    }

    async openProject() {
        this.error = null;
        const path = await open({
            multiple: false,
            directory: false,
            filters: [{ name: "Scramble Project", extensions: ["scramble"] }],
        });
        if (!path || Array.isArray(path)) return;

        try {
            const data = await invoke<ProjectData>("open_project", { path });
            this.apply(path, data);
        } catch (e) {
            this.error = String(e);
        }
    }

    closeProject() {
        this.path = null;
        this.name = null;
        this.sourceCount = 0;
        this.codeCount = 0;
        this.lastSaved = null;
        this.error = null;
    }

    private apply(path: string, data: ProjectData) {
        this.path = path;
        this.name = data.name;
        this.sourceCount = data.sources.length;
        this.codeCount = data.codes.length;
        this.lastSaved = new Date();
    }
}

export const projectStore = new ProjectStore();
