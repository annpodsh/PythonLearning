"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any


def custom_range(mas: str, *args: Any):
    if len(args) == 1:
        index = mas.index(args[0])
        if index == -1:
            return mas
        else:
            return mas[:index]
    elif len(args) == 2:
        start_index = mas.index(args[0])
        end_index = mas.index(args[1])
        if start_index == -1 or end_index == -1:
            return mas
        else:
            return mas[start_index:end_index]
    elif len(args) > 2:
        start_index = mas.index(args[0])
        end_index = mas.index(args[1])
        if start_index == -1 or end_index == -1 or type(args[2]) == isinstance(args[2], int):
            return mas
        else:
            return mas[start_index:end_index:args[2]]
    else:
        return mas


print(custom_range("abcdef", "d", "a", -2))