import { save, open, confirm as confirmDialog } from "@tauri-apps/plugin-dialog";
import { invoke } from "@tauri-apps/api/core";

export type SourceFolder = {
    id: string;
    name: string;
    parentId: string | null;
};

export type SourceDocument = {
    id: string;
    title: string;
    content: string;
    folderId: string | null;
    createdAt: string;
};

type ProjectData = {
    name: string;
    created_at: string;
    sources: SourceDocument[];
    codes: unknown[];
    folders: SourceFolder[];
};

class ProjectStore {
    name = $state<string | null>(null);
    path = $state<string | null>(null);
    createdAt = $state<string | null>(null);
    sources = $state<SourceDocument[]>([]);
    folders = $state<SourceFolder[]>([]);
    codes = $state<unknown[]>([]);
    lastSaved = $state<Date | null>(null);
    dirty = $state(false);
    error = $state<string | null>(null);

    sourceCount = $derived(this.sources.length);
    codeCount = $derived(this.codes.length);

    async newProject() {
        if (!(await this.confirmDiscard())) return;
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
        if (!(await this.confirmDiscard())) return;
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

    async closeProject() {
        if (!(await this.confirmDiscard())) return;
        this.path = null;
        this.name = null;
        this.createdAt = null;
        this.sources = [];
        this.folders = [];
        this.codes = [];
        this.lastSaved = null;
        this.dirty = false;
        this.error = null;
    }

    async saveProject() {
        if (!this.path || this.name === null) return;
        try {
            await invoke("save_project", {
                path: this.path,
                data: {
                    name: this.name,
                    created_at: this.createdAt,
                    sources: this.sources,
                    codes: this.codes,
                    folders: this.folders,
                },
            });
            this.lastSaved = new Date();
            this.dirty = false;
        } catch (e) {
            this.error = String(e);
        }
    }

    /** Resolves to whether the caller may proceed, prompting the user if there are unsaved changes. */
    async confirmDiscard(
        message = "You have unsaved changes. Discard them and continue?",
    ): Promise<boolean> {
        if (!this.dirty) return true;
        return await confirmDialog(message, {
            title: "Unsaved changes",
            kind: "warning",
        });
    }

    addFolder(name: string, parentId: string | null = null): SourceFolder {
        const folder: SourceFolder = { id: crypto.randomUUID(), name, parentId };
        this.folders = [...this.folders, folder];
        this.dirty = true;
        return folder;
    }

    renameFolder(id: string, name: string) {
        this.folders = this.folders.map((f) =>
            f.id === id ? { ...f, name } : f,
        );
        this.dirty = true;
    }

    deleteFolder(id: string) {
        const idsToRemove = this.collectFolderIds(id);
        this.folders = this.folders.filter((f) => !idsToRemove.has(f.id));
        this.sources = this.sources.filter(
            (s) => !s.folderId || !idsToRemove.has(s.folderId),
        );
        this.dirty = true;
    }

    addSource(
        title: string,
        content: string,
        folderId: string | null = null,
    ): SourceDocument {
        const doc: SourceDocument = {
            id: crypto.randomUUID(),
            title,
            content,
            folderId,
            createdAt: new Date().toISOString(),
        };
        this.sources = [...this.sources, doc];
        this.dirty = true;
        return doc;
    }

    deleteSource(id: string) {
        this.sources = this.sources.filter((s) => s.id !== id);
        this.dirty = true;
    }

    private collectFolderIds(id: string): Set<string> {
        const ids = new Set([id]);
        let changed = true;
        while (changed) {
            changed = false;
            for (const f of this.folders) {
                if (f.parentId && ids.has(f.parentId) && !ids.has(f.id)) {
                    ids.add(f.id);
                    changed = true;
                }
            }
        }
        return ids;
    }

    private apply(path: string, data: ProjectData) {
        this.path = path;
        this.name = data.name;
        this.createdAt = data.created_at;
        this.sources = data.sources ?? [];
        this.folders = data.folders ?? [];
        this.codes = data.codes ?? [];
        this.lastSaved = new Date();
        this.dirty = false;
    }
}

export const projectStore = new ProjectStore();
