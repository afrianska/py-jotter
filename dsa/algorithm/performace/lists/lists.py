# Import the timeit module
# import timeit

# Import the Timer class defined in the module
from timeit import Timer


def test1():
    new_list = []
    for i in range(1000):
        new_list = new_list + [i]
    return new_list


def test2():
    new_list = []
    for i in range(1000):
        new_list.append(i)
    return new_list


def test3():
    new_list = [i for i in range(1000)]
    return new_list


def test4():
    new_list = list(range(1000))
    return new_list


t1 = Timer("test1()", "from __main__ import test1")
print("contcat: ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append: ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension: ", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range: ", t4.timeit(number=1000), "milliseconds")
