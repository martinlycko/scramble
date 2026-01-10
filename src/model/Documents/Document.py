class Document():

    def __init__(self, id, title, content, notes, attributes):
        self.id = id
        self.title = title
        self.content = content
        self.notes = notes
        self.attributes = attributes

    @classmethod
    def from_dict(cls, data):
        print("Loading document " + data.get("title") +" with ID " + str(data.get("id")))
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            content=data.get("content", ""),
            notes=data.get("notes", ""),
            attributes=data.get("attributes", {})
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "notes": self.notes,
            "attributes": self.attributes
        }

    def update_content(self, notes, attributes):
        self.notes = notes
        self.attributes = attributes
    