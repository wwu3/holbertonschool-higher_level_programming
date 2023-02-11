#!/usr/bin/python3
"""Class to JSON"""


import json


def class_to_json(obj):
    """
    define a function class_to_json pass in the argument obj
    """
    return json.dumps(obj.__dict__)
