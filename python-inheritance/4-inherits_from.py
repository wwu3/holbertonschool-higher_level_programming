#!/usr/bin/python3
"""Represents subclass"""


def inherits_from(obj, a_class):
    """
    Defines a functiion called inherits_from
    """
    if issubclass(type(obj), type(obj)):
        return True
    return False
