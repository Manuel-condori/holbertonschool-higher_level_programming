#!/usr/bin/python3
"""defines a class called Square"""


class Square:

    """represents a square"""

    def __init__(self, size=0):

        """declaration the data
        args:
            size: size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):

        """returns the current square area"""

        return(self.__size ** 2)
