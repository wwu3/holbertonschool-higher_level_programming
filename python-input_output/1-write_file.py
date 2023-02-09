#!/usr/bin/python3
"""Write a file"""


def write_file(filename="", text=""):
    """
    define a function write_file with arguments filename, text
    """    
    with open(filename, 'w', encoding="utf-8") as f:
        s = str(text)
        f.write(s)
