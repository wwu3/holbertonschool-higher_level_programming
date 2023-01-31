#!/usr/bin/python3
"""Define a class Square"""


class Square:

    """Initializes the data"""
    def __init__(self, size=0):
        self.__size = size

        if not type(size) is int:
            print("size must be an integer", end='')
            raise TypeError
        else:
            if size < 0:
                print("size must be >= 0", end='')
                raise ValueError
