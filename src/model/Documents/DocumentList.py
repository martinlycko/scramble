from src.model.Documents.Document import Document

class DocumentList():

    def __init__(self):
        self.id = 0
        self.list = []

    @classmethod
    def from_dict(cls, data):
        document_list = cls()
        document_list.id = data.get("id", 0)
        for doc_data in data.get("documents", []):
            document = Document.from_dict(doc_data)
            document_list.list.append(document)
        return document_list

    def to_dict(self):
        return {
            "id": self.id,
            "documents": [doc.to_dict() for doc in self.list]
        }

    def add_document(self, title, content, notes, attributes):
        new_document = Document(self.id, title, content, notes, attributes)
        self.list.append(new_document)
        self.id += 1
        print(f"Document '{title}' added with ID {new_document.id}.")
        return new_document

    def get_document(self, id):
        for doc in self.list:
            if doc.id == id:
                return doc
        return None