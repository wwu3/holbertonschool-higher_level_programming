#!/usr/bin/python3
"""Define a class Base"""


class Base:
    """
    Attributes:
        __nb_objects    private class attribute
    """
    __nb_objects = 0

    """Initializes the data"""
    def __init__(self, id=None):
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        elif id is None:
            self.id = Base.__nb_objects
