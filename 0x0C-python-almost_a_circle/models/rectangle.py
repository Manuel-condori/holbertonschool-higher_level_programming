#!/usr/bin/python3
"""class Rectangle thet inherits drom class Base"""
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def typeChecker(self, name, value):
        """ integer validation check """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def valueWHChecker(self, name, value):
        """ width and height validation check """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def valueXYChecker(self, name, value):
        """ x and y validation check """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter, gets validated """
        self.typeChecker("width", value)
        self.valueWHChecker("width", value)
        self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter, gets validated """
        self.typeChecker("height", value)
        self.valueWHChecker("height", value)
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ X setter, gets validated """
        self.typeChecker("x", value)
        self.valueXYChecker("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y setter, gets validated """
        self.typeChecker("y", value)
        self.valueXYChecker("y", value)
        self.__y = value

    def area(self):
        """calculates the area"""
        return self.width * self.height

    def display(self):
        """Prints a representation of the rectangle with '#'"""

        for space in range(self.__y):
            print("")

        for row in range(self.__height):
            for move in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Overrides the __str__ method so it returns something else"""
        return("[{}] ({}) {}/{} - {}/{}".format(
            str(self.__class__.__name__), self.id, self.x,
            self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ the update function
        Args:
            *args: multiple arguments
            **kwargs: dictionary arguments
        """
        if args is not None and len(args) > 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.width = value
                elif index == 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                elif index == 4:
                    self.y = value
                elif index >= 5:
                    raise Exception("Too many arguments")
        else:
            for key, date in kwargs.items():
                if key == "id":
                    self.id = date
                elif key == "width":
                    self.width = date
                elif key == "height":
                    self.height = date
                elif key == "x":
                    self.x = date
                elif key == "y":
                    self.y = date

    def to_dictionary(self):
        """ returns the dict representation of a rect """
        temp = dict()
        temp['id'] = self.id
        temp['width'] = self.width
        temp['height'] = self.height
        temp['x'] = self.x
        temp['y'] = self.y
        return temp                    
