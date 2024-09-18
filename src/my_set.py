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

    def discard(self, element):
        if element in self._elements:
            self._elements.remove(element)

    def union(self, iterable):
        union_set = Set(self._elements)
        union_set.update(iterable)
        return union_set
    
    def intersection(self, iterable):
        intersection_set = Set()
        for element in self._elements:
            if element in iterable:
                intersection_set.add(element)
        return intersection_set