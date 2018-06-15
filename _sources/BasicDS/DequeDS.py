class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def add_front(self, item):
        return self.items.append(item)

    def add_rear(self, item):
        return self.items.insert(0, item)

    def remove_from(self, item):
        return self.items.pop()

    def remove_rear(self, item):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
