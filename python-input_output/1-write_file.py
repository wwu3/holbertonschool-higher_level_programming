#!/usr/bin/python3
"""Write a file"""


def write_file(filename="", text=""):
    """
    define a function write_file with arguments filename, text
    """ 
    count = 0   
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
