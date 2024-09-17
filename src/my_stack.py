class Stack():
    def __init__(self, max_size=None):
        self.quantity = 0
        self.storage = {}
        self.max_size = max_size

    def push(self, item):
        if self.max_size is not None and self.quantity == self.max_size:
            return "Stack storage is full"
        self.storage[self.quantity] = item
        self.quantity += 1

    def pop(self):
        if self.quantity == 0:
            return "Stack is empty"
        item_to_remove = self.storage[self.quantity - 1]
        del self.storage[self.quantity - 1]
        self.quantity -= 1
        return item_to_remove