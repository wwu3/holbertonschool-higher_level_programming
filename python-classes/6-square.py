#!/usr/bin/python3
"""Define a class Square"""


class Square:

    """Initializes the data"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not type(value[0]) is int) or (not type(value[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        else:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for row in range(self.__size):
            print("#" * self.__size)
        if self.__position[1] > 0:
            print("--")
