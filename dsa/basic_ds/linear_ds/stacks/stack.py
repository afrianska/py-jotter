# Stack 1
class Stack1:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Stack 2
class Stack2:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)  # This will be affected on performance

    def pop(self):
        return self.items.pop(0)  # This will be affected on performance

    def peek(self):
        return self.items[0]  # This will be affected on performance

    def size(self):
        return len(self.items)
