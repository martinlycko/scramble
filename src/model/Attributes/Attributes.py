class Attributes():

    def __init__(self):
        self.list = []

    @classmethod
    def from_dict(cls, data):
        attributes = cls()
        for attr in data.get("list", []):
            print("Loading attribute: " + str(attr))
            attributes.list.append(attr)
        return attributes

    def to_dict(self):
        return {
            "list": [
                item.to_dict() if hasattr(item, "to_dict") else item
                for item in self.list
            ]
        }

    def add(self, name):
        for attr in self.list:
            if attr == name:
                return False
        self.list.append(name)
        return True