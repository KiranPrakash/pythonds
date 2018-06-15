class BinaryTree:
    def __init__(self, root_object):
        self.key = root_object
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)

        else:
            temp = BinaryTree(new_node)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)

        else:
            temp = BinaryTree(new_node)
            temp.right_child = self.right_child
            self.right_child = temp

    def get_root_value(self):
        return self.key

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_value(self, new_value):
        self.key = new_value


def main():
    r = BinaryTree('a')
    print(r.left_child)
    r.insert_left('b')
    r.insert_right('c')
    print(r.get_left_child().get_root_value(), r.get_right_child().get_root_value())
    r.get_right_child().set_root_value("Hello World")

    print(r.get_right_child().get_root_value())

    x = BinaryTree('a')
    x.insert_left('b')
    x.insert_right('c')
    x.get_left_child().insert_right('d')
    x.get_right_child().insert_left('f')
    x.get_right_child().insert_right('e')


if __name__ == '__main__':
    main()






