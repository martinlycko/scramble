import { Doc } from "./datamodel/Doc";
import { Theme } from "./datamodel/Theme";
import { Code } from "./datamodel/Code";

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

    //Coded snippets
    public codes: Code[];

    public constructor() {
        this.name = null
        this.file = null;
        this.documents = $state([]);
        this.doc_max_id = 0;
        this.themes = $state([]);
        this.themes_max_id = 0;
        this.codes = $state([]);
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

    public addCode(documentID: Number, themeID: Number, content: String) {
        const newCode = new Code(documentID, themeID, content);
        this.codes.push(newCode);
        console.log("Added code snippet:", newCode);
    }

    public getThemeById(id: Number): Theme | null {
        for (let theme of this.themes) {
            if (theme.id === id) { 
                return theme;
            }
        }        return null;
    }

    getCodedDocIDsForTheme(themeID: Number): Number[] {
        return [...new Set(this.codes
            .filter(code => code.themeID === themeID)
            .map(code => code.documentID))];
    }

    getCodesByThemeAndDoc(themeID: Number, documentID: Number): Code[] {
        return this.codes.filter(code => code.themeID === themeID && code.documentID === documentID);
    }

}

export const project = new Project();