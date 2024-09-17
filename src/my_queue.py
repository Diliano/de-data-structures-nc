class Queue():
    def __init__(self, max_size=None):
        self.max_size = max_size
        self._front = 0
        self._back = 0
        self._storage = {}

    def enqueue(self, item):
        if self.max_size is not None and len(self._storage) == self.max_size:
            return "Queue is full"
        self._storage[self._back] = item
        self._back += 1

    def dequeue(self):
        if len(self._storage) == 0:
            return "Queue is empty"
        del self._storage[self._front]
        self._front += 1

    def get_quantity(self):
        return len(self._storage)
    
    def is_empty(self):
        return len(self._storage) == 0
    
    def is_full(self):
        return len(self._storage) == self.max_size