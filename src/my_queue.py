class Queue():
    def __init__(self, max_size=None):
        self.max_size = max_size
        self._front = 0
        self._back = 0
        self._storage = {}