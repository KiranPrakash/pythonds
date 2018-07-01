import random

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node

    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

    if root.val >= node.val:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

def search(root, key):
    if root is None or root.val == key:
        print("Found key: ", key)
        return root
    if root.val < key:
        search(root.right, key)
    else:
        search(root.left, key)
    return False

def minimum(root):
    if root is None or root.left is None:
        return root
    return minimum(root.left)

def maximum(root):
    if root is None or root.right is None:
        return root
    return maximum(root)

def inorder_successor(root, node):
    """1. if the right subtree of the node is not None, then succcessor lies in the right subtree; go to the right subtree and find
    the minimum key value in the right subtree.

    2. If the node does not have right subtree, search that node P from root, the node from where
     we take the last left is the answer"""
    if root is not None or root.right is not None:
        return minimum(root.right)

    succ = None
    while root.val != node.val:
        if root.val > node.val:
            succ = root
            root = root.left
        else:
            root = root.right
    return succ

def inorder_predecessor(root, node):
    """
    1. If the left subtree of the node is not None, then the predecessor lies in the left subtree,
    to find it, go to the maximum key value in the left subtree
    2. if the left subtree is none, then search for the node from the root, the node from where we take last right is the answer


    :param root:
    :param node:
    :return:
    """
    if root is not None or root.left is not None:
        return maximum(root.left)

    pred = None
    while(root.val != node.val):
        if root.val > node.val:
            root = root.left
        else:
            pred = root
            root = root.right
    return pred


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.val)

def parent(root, node):
    if root is None:
        return root

    elif (root.left is not None and root.left.val == node.val)\
            or (root.right is not None and root.right.val == node.val):
        return root.val
    else:
        if root.val < node.val:
            return parent(root.right, node)
        else:
            return parent(root.left, node)

def delete_node(root, node):
    """
    Could be done with a parent pointer or without it.
    If the node to be deleted has
    1. no child or one child
        - Just delete the node

    3, two child
        - find the inorder successor of the right sub tree and replace it to the node to be deleted

    :param root:
    :param node:
    :return:
    """
    if root is None:
        return root

    elif root.val < node.val:
        root.right = delete_node(root.right, node)

    elif root.val > node.val:
        root.left = delete_node(root.left, node)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minimum(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp)

    return root

"""
x = Node(51)

for i in range(32):
    insert(x, Node(random.randint(1,100)))

inorder(x)

search(x, Node(28))

"""

r = Node(50)
insert(r, Node(18))
insert(r, Node(70))
insert(r, Node(80))
insert(r, Node(65))
insert(r, Node(25))
insert(r, Node(15))
insert(r, Node(40))
insert(r, Node(10))
insert(r, Node(68))
insert(r, Node(20))
insert(r, Node(90))
insert(r, Node(75))
insert(r, Node(30))
insert(r, Node(68))


delete_node(r, Node(25))
inorder(r)

