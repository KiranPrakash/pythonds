from StackDS import Stack

def check_parantheses(string):

    s = Stack()
    balanced = True
    index = 0

    while index < len(string) and balanced:
        if string[index] == '(':
            s.push(string[index])

        else:
            if s.isEmpty():
                balanced = False

            else:
                s.pop()

        index += 1

    if balanced and s.isEmpty():
        return True

    else:
        return False


print(check_parantheses('((()))'))
print(check_parantheses('(((((((()))))))'))