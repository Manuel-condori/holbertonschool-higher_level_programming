#!/usr/bin/python3
"""Module holds class Base"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes attributes for class Base
        Args:
            id: public instance attribute
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns JSON of a dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
