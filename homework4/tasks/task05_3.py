"""
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests

* https://en.wikipedia.org/wiki/Fizz_buzz
"""
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    """
    >>> list(fizzbuzz(10))
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
    >>> list(fizzbuzz(5))
    ['1', '2', 'Fizz', '4', 'Buzz']
    """
    for i in range(1, n + 1):
        yield "Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i)
