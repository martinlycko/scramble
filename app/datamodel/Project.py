from .Document import Document as Doc

class Project:
    def __init__(self, name, description):
        # Project attributes
        self.name: str = name
        self.description: str = description

        # Documents
        self.documents: list[Doc] = []
        self.doc_max_id: int = 0

        # Themes
        self.themes: list[str] = []

    def add_document(self, title: str, content: str) -> Doc:
        self.doc_max_id += 1
        new_doc = Doc(self.doc_max_id, title, content)
        self.documents.append(new_doc)
        return new_doc
    
    def get_document_by_id(self, doc_id: int) -> Doc | None:
        for doc in self.documents:
            if doc.id == doc_id:
                return doc
        return None
    
    def add_theme(self, theme: str) -> None:
        self.themes.append(theme)
        return None