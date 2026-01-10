from src.model.Themes.Theme import Theme

class ThemeList():

    def __init__(self):
        self.id = 0
        self.list = []

    @classmethod
    def from_dict(cls, data):
        theme_list = cls()
        theme_list.id = data.get("id", 0)
        for doc_data in data.get("themes", []):
            document = Theme.from_dict(doc_data)
            theme_list.list.append(document)
        return theme_list

    def to_dict(self):
        return {
            "id": self.id,
            "themes": [doc.to_dict() for doc in self.list]
        }
    
    def add_theme(self, title):
        new_theme = Theme(self.id, title)
        self.list.append(new_theme)
        self.id += 1
        print(f"Theme '{title}' added with ID {new_theme.id}.")
        return new_theme