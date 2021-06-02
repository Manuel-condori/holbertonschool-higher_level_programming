#!/usr/bin/python3
"""Module holds a function that determines if an object is an instance of a
class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """Args:
        obj: The object to check
        a_class: The class to check against
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
