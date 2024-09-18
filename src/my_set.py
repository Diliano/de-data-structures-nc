class Set():
    def __init__(self, elements=None):
        self._elements = []
        if elements:
            self.update(elements)

    def add(self, element):
        if element not in self._elements:
            self._elements.append(element)

    def update(self, iterable):
        for element in iterable:
            self.add(element)