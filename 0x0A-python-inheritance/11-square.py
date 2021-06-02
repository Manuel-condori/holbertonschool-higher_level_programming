#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):

        return self.__size ** 2

    def __str__(self):

        return "[Square] {0}/{0}".format(self.__size)
