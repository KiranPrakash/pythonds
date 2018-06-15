from StackDS import Stack

def divideby2(decimal_numb):
    remainder_stack = Stack()

    while decimal_numb>0:
        remainder = decimal_numb % 2

        remainder_stack.push(remainder)

        decimal_numb //=2
    bin_string = []
    while not remainder_stack.isEmpty():
        bin_string += str(remainder_stack.pop())

    return bin_string

print(divideby2(23))

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString