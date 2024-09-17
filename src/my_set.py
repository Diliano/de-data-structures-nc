class Set():
    def __init__(self):
        self._elements = []

    def add(self, element):
        if element in self._elements:
            return "No duplicates allowed"
        self._elements.append(element)