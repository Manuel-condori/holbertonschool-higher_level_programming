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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 'json_string'
        Args:
            json_string: is a string representing a list of dictionaries
        """

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            **dictionary: can be thought of as a double pointer to a
                          dictionary
        """
        if cls.__name__ == "Rectangle":
            temp = cls(width=6, height=9)
        if cls.__name__ == "Square":
            temp = cls(size=69)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        temp = []
        try:
            with open("{}.json".format(
                    cls.__name__), "r", encoding='utf-8') as f:
                temp2 = cls.from_json_string(f.read())
        except:
            return list()
        for i in temp2:
            temp.append(cls.create(**i))
        return temp
