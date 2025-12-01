import { Doc } from "./datamodel/Doc";
import { Theme } from "./datamodel/Theme";
import { Code } from "./datamodel/Code";

class Project {
    
    //Project metadata
    public loaded: boolean = false;
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

    public toJSON(): any {
        return {
            __type: "Project",
            loaded: this.loaded,
            name: this.name,
            file: this.file,
            doc_max_id: this.doc_max_id,
            themes_max_id: this.themes_max_id,

            // Convert each subclass to JSON using its own toJSON()
            documents: this.documents.map(doc => doc.toJSON()),
            themes: this.themes.map(theme => theme.toJSON()),
            codes: this.codes.map(code => code.toJSON())
        };
    }
    
    public loadFromFile(bytes: any) {
        // Decode the bytes to a string and parse the JSON
        const jsonString = new TextDecoder().decode(bytes);
        const data = JSON.parse(jsonString);

        // Set all values directly importable from JSON
        this.name = data.name;
        this.file = data.file;
        this.doc_max_id = data.doc_max_id;
        this.themes_max_id = data.themes_max_id;

        // Reconstruct subclass instances from JSON data
        this.documents = data.documents.map((docData: any) => Doc.fromJSON(docData));
        this.themes = data.themes.map((themeData: any) => Theme.fromJSON(themeData));
        this.codes = data.codes.map((codeData: any) => Code.fromJSON(codeData));
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

    removeDocumentById(id: Number) {
        this.documents = this.documents.filter(doc => doc.id !== id);
        this.codes = this.codes.filter(code => code.documentID !== id);
        console.log(`Removed document with ID ${id} and its associated codes.`);
    }

    removeThemeById(id: Number) {
        this.themes = this.themes.filter(theme => theme.id !== id);
        this.codes = this.codes.filter(code => code.themeID !== id);
        console.log(`Removed theme with ID ${id} and its associated codes.`);
    }

    renameThemeById(id: Number, newTitle: String) {
        const theme = this.getThemeById(id);
        if (theme) {
            theme.title = newTitle;
            console.log(`Renamed theme with ID ${id} to "${newTitle}".`);
        }   else { 
            console.log(`Theme with ID ${id} not found.`);
        }
    }

    renameDocumentById(id: Number, newTitle: String) {
        const document = this.getDocumentById(id);
        if (document) {
            document.title = newTitle;
            console.log(`Renamed document with ID ${id} to "${newTitle}".`);
        }   else { 
            console.log(`Document with ID ${id} not found.`);
        }
    }
}

export const project = new Project();