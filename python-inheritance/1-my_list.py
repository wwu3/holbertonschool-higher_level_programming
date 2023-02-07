#!/usr/bin/python3
"""Represents MyList"""


class MyList(list):
    """A class defined as MyList that inherits from super class called list"""
    def print_sorted(self):
        print(sorted(self))
