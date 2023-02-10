#!/usr/bin/python3
"""To JSON string"""


import json


def to_json_string(my_obj):
    """
    define a function to_json_string pass the argument my_obj
    """
    x = my_obj
    json.dumps(x)
    return str(x)
