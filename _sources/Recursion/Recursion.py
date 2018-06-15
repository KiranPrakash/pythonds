def printFunc(test):
    if test<1:
        return
    else:
        print(test, end=" ")
        printFunc(test-1)
        print(test, end=" ")
        return
"""
test = 3
printFunc(test)
"""

def equation1(x, y):
    if x == 0:
        return y
    else:
        return equation1(x-1, x+y)

solution = equation1(3, 4)
print(solution)


def equation2(n):
    if n == 1:
        return 0
    else:
        return 1+equation2(n/2)

print(equation2(8))
