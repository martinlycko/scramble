from src.model.Documents.DocumentList import DocumentList
from src.model.Attributes.Attributes import Attributes

class Project():

    def __init__(self):
        self.project_name = "Scramble Project"
        self.file_path = None

        self.documents = DocumentList()
        self.attributes = Attributes()

    def add_attribute(self, name):
        if self.attributes.add(name):
            for doc in self.documents.list:
                doc.attributes.update({name: None})
            return True
        else:
            return False
        
    def to_dict(self):
        return {
            "project_name": self.project_name,
            "file_path": self.file_path,
            "documents": self.documents.to_dict(),
            "attributes": self.attributes.to_dict()
        }