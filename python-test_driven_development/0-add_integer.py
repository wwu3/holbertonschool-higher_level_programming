#!/usr/bin/python3
# doctest_0-add_integer.py
"""
This is the "example" module.

The  module supplies one function, add_integer().  Eg,

>>>add_integer(2, 98)
100
"""


def add_integer(a, b=98):
    """
    Returns a + b.
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a+b)

# doctest_tracebacks.py


def this_raises():
    """This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> this_raises()
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """
    raise RuntimeError('here is the error')
