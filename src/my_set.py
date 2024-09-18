class Set():
    def __init__(self):
        self._elements = []

    def add(self, element):
        if element not in self._elements:
            self._elements.append(element)

    def update(self, iterable):
        for element in iterable:
            self.add(element)