#!/usr/bin/python3
"""Define a class Base"""
import json


class Base:
    """
    Attributes:
        __nb_objects    private class attribute
    """
    __nb_objects = 0

    """Initializes the data"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        elif id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def get_nb_objects():
        return Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)
