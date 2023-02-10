#!/usr/bin/python3
"""From Json string to Object"""


import json


def from_json_string(my_str):
    """
    define a function from_json_string passing the argument my_str
    """
    return json.loads(my_str)
