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
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class Method save_to_file
        """
        if list_objs is None:
            list_objs = []
        with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as f:
            list_dicts = [o.to_dictionary() for o in list_objs]
            f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        i = cls(1, 2)
        i.update(**dictionary)
        return i

    @classmethod
    def load_from_file(cls):
        with open(f"{cls.__name__}.json", 'r', encoding="utf-8") as f:
            json_string = f.read()
            list_of_dictionaries = Base.from_json_string(json_string)
        return [cls.create(**i) for i in list_of_dictionaries]
