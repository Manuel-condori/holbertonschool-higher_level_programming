#!/usr/bin/python3

"""Módulo para 0-add_integer. Contiene la función add_integer que suma\
        dos enteros y devuelve su suma
"""


def add_integer(a, b=98):
    """
    Args:
        a = the first integer
        b = the second integer
    Return:
        The sum of a and b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
