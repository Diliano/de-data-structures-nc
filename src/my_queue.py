class QueueFullError(Exception):
    def __init__(self):
        self.message = "Queue is full"
        super().__init__(self.message)

class QueueEmptyError(Exception):
    def __init__(self):
        self.message = "Queue is empty"
        super().__init__(self.message)

class Queue():
    """
    max_size is optional and where not provided by the user, it will 
    default to None (no maximum size)
    """
    def __init__(self, max_size=None):
        self.max_size = max_size
        self._front = 0
        self._back = 0
        self._storage = {}

    def enqueue(self, item):
        if self.max_size is not None and len(self._storage) == self.max_size:
            raise QueueFullError
        self._storage[self._back] = item
        self._back += 1

    def dequeue(self):
        if len(self._storage) == 0:
            raise QueueEmptyError
        del self._storage[self._front]
        self._front += 1

    def get_quantity(self):
        return len(self._storage)
    
    def is_empty(self):
        return len(self._storage) == 0
    
    def is_full(self):
        return len(self._storage) == self.max_size