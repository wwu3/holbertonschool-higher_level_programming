#!/usr/bin/python3
"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """
    define a function load_from_json_file passing the argument filename
    """
    with open(filename, 'r', encoding="utf-8") as f:
        x = json.loads(f.read())
    return x
