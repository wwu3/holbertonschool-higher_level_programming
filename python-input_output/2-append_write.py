#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """
    define a function append_write
    """
    count = 0 
    with open(filename, 'a+', encoding="utf-8") as f:
        count = f.write(text)
    return count
