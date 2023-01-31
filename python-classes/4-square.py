#!/usr/bin/python3
"""Define a class Square"""


class Square:

    """Initializes the data"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            print("size must be an integer", end='')
            raise TypeError
        else:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        return self.__size * self.__size
