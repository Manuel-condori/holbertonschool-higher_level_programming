#!/usr/bin/python3
"""This module holds a function that checks if an object is an instance
or a specified class
"""


def is_same_class(obj, a_class):
    return type(obj) == a_class
