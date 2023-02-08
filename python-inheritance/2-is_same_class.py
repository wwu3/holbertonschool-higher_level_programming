#!/usr/bin/python3
"""Represents the same object"""


def is_same_class(obj, a_class):
    return isinstance(type(obj), type(a_class))
