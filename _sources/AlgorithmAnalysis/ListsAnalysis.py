def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l= list(range(1000))


from timeit import Timer

# t1 = Timer("test1()", "from __main__ import test1")
# print("concat", t1.timeit(number=1000),"milliseconds")
# t2 = Timer("test2()", "from __main__ import test2")
# print("append", t2.timeit(number=1000),"milliseconds")
#
# t3 = Timer("test3()", "from __main__ import test3")
# print("list comprehension", t3.timeit(number=1000),"milliseconds")
# t4 = Timer("test4()", "from __main__ import test4")
# print("list", t4.timeit(number=1000),"milliseconds")


import random

for i in range(10000, 1000001, 20000):
    t = Timer("random.randrange(%d) in x "%i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("{}, {}, {}".format(i, lst_time,d_time))


