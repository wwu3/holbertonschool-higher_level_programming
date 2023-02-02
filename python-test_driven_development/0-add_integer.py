#!/usr/bin/python3
"""
What
is
words
"""


def add_integer(a, b=98):
    """
    What thet
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("a must be an integer")

    return int(a+b)
