import { Doc } from "./datamodel/Doc";
import { Theme } from "./datamodel/Theme";

class Project {
    
    //Project metadata
    public name: String | null;
    public file: String | null;

    //Document list
    public documents: Doc[];
    doc_max_id: Number;

    //Theme list
    public themes: Theme[];
    themes_max_id: Number; 

    public constructor() {
        this.name = null
        this.file = null;
        this.documents = $state([]);
        this.doc_max_id = 0;
        this.themes = $state([]);
        this.themes_max_id = 0;
    }

    public addDocument(title: String, text: String) {
        this.doc_max_id = this.doc_max_id.valueOf() + 1;
        const newDoc = new Doc(this.doc_max_id, title, text);
        this.documents.push(newDoc);
        console.log("Added document:", newDoc);
    }

    public getDocumentById(id: Number): Doc | null {
        for (let doc of this.documents) {
            if (doc.id === id) {
                return doc;
            }
        }
        return null;
    }

    public addTheme(title: String) {
        this.themes_max_id = this.themes_max_id.valueOf() + 1;
        const newTheme = new Theme(this.themes_max_id, title);
        this.themes.push(newTheme);
        console.log("Added theme:", newTheme);
    }
}

export const project = new Project();