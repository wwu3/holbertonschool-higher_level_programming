#!/usr/bin/python3
"""Represents a Geometry"""


class BaseGeometry:
    """A class defined as BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("name must be an integer")
        else:
            if value < 0:
                raise ValueError("distance must be greater than 0")
            elif value == 0:
                raise ValueError("age must be greater than 0")
