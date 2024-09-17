class Stack():
    def __init__(self, max_size=None):
        self.quantity = 0
        self.storage = {}
        self.max_size = max_size