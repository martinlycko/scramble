class Document():

    def __init__(self, id, title, content, notes, attributes):
        self.id = id
        self.title = title
        self.content = content
        self.notes = notes
        self.attributes = attributes

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "notes": self.notes,
            "attributes": self.attributes
        }

    