class Theme():

    def __init__(self, id, title):
        self.id = id
        self.title = title

    @classmethod
    def from_dict(cls, data):
        print("Loading theme " + data.get("title") +" with ID " + str(data.get("id")))
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
        }