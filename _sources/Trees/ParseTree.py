import sys
sys.path.append('/home/kiran/PycharmProjects/pythonds/_sources')
from BasicDS.StackDS import Stack
from BinaryTree import BinaryTree
import BasicDS.operator

def parse_tree(expression):
    token_list = expression.split()
    parent_stack = Stack()
    empty_tree = BinaryTree('')
    parent_stack.push(empty_tree)
    current_tree = empty_tree

    for i in token_list:
        if i == '(':
            current_tree.insert_left('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['+', '*', '/', '-']:
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            parent_stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = parent_stack.pop()

        elif i not in ['+', '*', '/', '-']:
            try:
                current_tree.set_root_value(int(i))
                current_tree = parent_stack.pop()
            except ValueError:
                raise ValueError("token '{}' is not a valid integet".format(i))

        return empty_tree


def evaluate(parse_tree):
    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    left_ch = parse_tree.get_left_child()
    right_ch = parse_tree.get_right_child()

    if left_ch and right_ch:
        func = operators[parse_tree.get_root_value()]
        return func(evaluate(left_ch),evaluate(right_ch))
    else:
        return parse_tree.get_root_value


def postordereval(tree):
    operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    result1 = None
    result2 = None

    if tree:
        result1 = postordereval(tree.get_left_child())
        result2 = postordereval(tree.get_right_child())
        if result1 and result2:
            return operators[tree.get_root_value()](result1, result2)
        else:
            return tree.get_root_value() #this is the base case for the recursive, this would be the one of the operator

def printexp(tree):
    sval = ""
    if tree:
        sval = '(' + printexp(tree.get_left_child())
        sval =  sval + str(tree.get_root_value())
        sval =  sval + printexp(tree.get_right_child())+')'
    return sval



some_tree = parse_tree(" ( 3 + ( 4 * 5 ) ) ")
#some_tree.postorder()
evaluate(some_tree)



