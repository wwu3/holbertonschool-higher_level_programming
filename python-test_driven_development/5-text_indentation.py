#!/usr/bin/python3
"""
This is a text_indentation module.
The module supplies a text_indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after characters ., ? and :
    """
    if not type(text) is str:
        raise TypeError("text must be a string")
    else:
        for a in text:
            print("{}".format(a), end='')
            if a == "." or a == "?" or a == ":":
                print()
                print()
