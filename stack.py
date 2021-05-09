class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if len(self.items) > 0:
            return False
        return True

    def clear(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            removedItem = self.items.pop(len(self.items)-1)
            return removedItem
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]
        return None
