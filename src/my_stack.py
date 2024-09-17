class Stack():
    def __init__(self, max_size=0):
        self.quantity = 0
        self.storage = {}
        self.max_size = max_size