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

    public addCode(documentID: Number, themeID: Number, content: String, startPos: Number, endPos: Number, length: Number) {
        const existingCodes = this.getCodesByThemeAndDoc(themeID, documentID);
        for (let code of existingCodes) {
            //New code is a perfect subset of an existing code
            if (code.startPos <= startPos && code.endPos >= endPos) {
                console.log("Code snippet is a subset of an existing code. Not adding.");
                return;
            }
            //New code is perfect superset of an existing code
            if (code.startPos >= startPos && code.endPos <= endPos) {
                //Remove the existing code
                this.codes = this.codes.filter(c => c !== code);
                console.log("Removed existing code snippet as it is a subset of the new code:", code);
                continue;
            }
            //New code overlaps with an existing code - expands to the right
            if (code.startPos < startPos && code.endPos > startPos && code.endPos < endPos) {
                content = code.content.substring(0, startPos.valueOf() - code.startPos.valueOf()) + content;
                startPos = code.startPos;
                length = endPos.valueOf() - startPos.valueOf();
                console.log("Code snippet expanded existing code to the right. Removed old cold.");
                this.codes = this.codes.filter(c => c !== code);
            }
            //New code overlaps with an existing code - expands to the left
            if (code.startPos > startPos && code.startPos < endPos && code.endPos > endPos) {
                content = content + code.content.substring(endPos.valueOf() - code.startPos.valueOf(), code.endPos.valueOf() - code.startPos.valueOf());
                endPos = code.endPos;
                length = endPos.valueOf() - startPos.valueOf();
                console.log("Code snippet expanded existing code to the left. Removed old cold.");
                this.codes = this.codes.filter(c => c !== code);
            }
        }
        //If none of the checks before have cought the code, add the code to the list
        const newCode = new Code(documentID, themeID, content, startPos, endPos, length);
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