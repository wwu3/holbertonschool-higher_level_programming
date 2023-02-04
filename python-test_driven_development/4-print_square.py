#!/usr/bin/python3
"""
This is the print_square module.

The module supplies one function, print_square().
"""


def print_square(size):
    """
    Prints square with character #
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")
        if float(size) < 0:
            raise TypeError("size must be an integer")
    st = "#"
    st = size * st + "\n"
    st = size * st
    print(st[:-1])
