from src.model.Documents.Document import Document

class DocumentList():

    def __init__(self):
        self.id = 0
        self.list = []

    def add_document(self, title, content):
        new_document = Document(self.id, title, content)
        self.list.append(new_document)
        self.id += 1
        print(f"Document '{title}' added with ID {new_document.id}.")

    def get_document(self, id):
        for doc in self.list:
            if doc.id == id:
                return doc
        return None