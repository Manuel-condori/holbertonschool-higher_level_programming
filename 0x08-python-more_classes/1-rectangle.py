#!/usr/bin/python3

"""define an Rectangle class"""


class Rectangle:
    """a rectangle class"""
    def __init__(self, width=0, height=0):
        """arg:
            property width
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
