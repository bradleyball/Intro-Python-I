# day 2 notes

# basic function declaration


def foo(x):
    return x + 1


print(foo(2))


def foo2(x):
    global a  # tells python a is global
    a = 5
    return x + a


# cant do
"""def foo3(x):
    total = 0

    def bar(y):
        total += y
    for i in range(x):
        bar(i)
    return total"""


# how to use scope one level up
def foo3(x):
    total = 0

    def bar(y):
        nonlocal total
        total += y
    for i in range(x):
        bar(i)
    return total


print(foo3(21))


# can use named arguments

def foo4(x, y, z):
    print(x, y, z)


foo4(z=1, y=2, x=3)


def sum(count, *args):
    print(count)
    print(args)


sum(3, 444, 44, 22)


def sum2(count, *args):
    a = 0
    for i in args:
        a += i
        return a


x = [11, 22, 33, 44]
print(sum2(3, *x))
print(sum2(3, 11, 22, 33, 44))

# keyword args


def foo8(**kwargs):
    print(kwargs)

    if kwargs['beej'] == 99:
        print(kwargs['y'])
    else:
        print(kwargs['x'])


foo8(x=10, y=20, beej=98)

# pass in dictionary with **d
# pass keyword does nothing


class Animal:
    pass


# how to construct new class
a = Animal()


class Animal2:
    def __init__(self):  # constructor, self is first thing called always
        self.leg_count = 4

    def get_leg_count(self):
        return self.leg_count

    def set_leg_count(self, c):
        self.leg_count = c


class Centipede(Animal):
    pass


a = Animal2()
a.set_leg_count(6)
print(a.get_leg_count())

"""
c = Centipede()
c.set_leg_count(6)
print(a.get_leg_count())"""
