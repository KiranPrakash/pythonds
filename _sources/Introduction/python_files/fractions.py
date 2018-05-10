""" Object Oriented Programming. A class to find Fractions given two numbers"""


def gcd(m,n):
    while m%n != 0:

        oldm = m
        oldn = n

        m = oldn

        n = oldm % oldn

    return n


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


f1 = Fraction(3, 5)
f2 = Fraction(15,10)
f3=f1+f2

print(f3)
print(f1==f2)
