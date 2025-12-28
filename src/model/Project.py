from src.model.Documents.DocumentList import DocumentList
from src.model.Attributes.Attributes import Attributes

class Project():

    def __init__(self):
        self.documents = DocumentList()
        self.attributes = Attributes()

    def add_attribute(self, name):
        if self.attributes.add(name):
            for doc in self.documents.list:
                doc.attributes.update({name: None})
            return True
        else:
            return False