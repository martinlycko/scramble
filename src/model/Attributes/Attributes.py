class Attributes():

    def __init__(self):
        self.list = []

    def add(self, name):
        for attr in self.list:
            if attr == name:
                return False
        self.list.append(name)
        return True