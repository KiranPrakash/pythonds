class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class StackRev:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    x = Stack()

    x.push(1)
    x.push(2)
    print(x.peek())
    print(x.isEmpty())

    y = StackRev()

    y.push('good')
    y.push('morning!')

    print(y.peek())
    print(y.pop())


if __name__ == '__main__':
    main()

