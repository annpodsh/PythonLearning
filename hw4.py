"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import Callable
from functools import lru_cache


def cache(func: Callable) -> Callable:
    return lru_cache()(lambda *args: func(*args))


def sum_of_2(x, y):
    return x + y


a = cache(sum_of_2)
print(a(1, 2))
print(a(2, 3))
print(a(1, 2))
print(a.cache_info())
