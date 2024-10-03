import math     # импортируем что будем использовать в глобальное пространство имен
# from math import *  - импортируем все в глобальное пространство имен

def square(x):
    d = x ** 2
    def even(x):
        nonlocal d  # не локальное пространство
        d = x / 2
        print(locals())
    even(x)
    return d

a = 5
b = square(4)
print(b)
print(math.sqrt(a))
print(globals())