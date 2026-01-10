class Attributes():

    def __init__(self):
        self.list = []

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