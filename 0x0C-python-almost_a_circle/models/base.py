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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file
        Args:
            list_objs: a list of instances who inherit of Base
        """
        fn = cls.__name__
        filename = fn + ".json"
        new_list = []
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                for obj in list_objs:
                    new_list.append(obj.to_dictionary())
                f.write(cls.to_json_string(new_list))
