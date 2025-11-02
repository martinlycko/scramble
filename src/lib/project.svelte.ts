import { Doc } from "./datamodel/Doc";

class Project {
    
    //Project metadata
    public name: String | null;
    public file: String | null;

    //Document list
    public documents: Doc[];
    public doc_max_id: Number;

    public constructor() {
        this.name = null
        this.file = null;
        this.documents = $state([]);
        this.doc_max_id = 0;
    }

    public addDocument(title: String, text: String) {
        this.doc_max_id = this.doc_max_id.valueOf() + 1;
        const newDoc = new Doc(this.doc_max_id, title, text);
        this.documents.push(newDoc);
        console.log("Added document:", newDoc);
    }
}

export const project = new Project();