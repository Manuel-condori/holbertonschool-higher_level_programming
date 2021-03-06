#!/usr/bin/python3
""" module that holds the square class. inherits from rect """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ all sides same size """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializer """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ overwrites the str """
        return("[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ the getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter """
        self.typeChecker("width", value)
        self.valueWHChecker("width", value)
        self.width = value

        self.typeChecker("height", value)
        self.valueWHChecker("height", value)
        self.height = value

    def update(self, *args, **kwargs):
        """ the update method """
        if args is not None and len(args) > 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value
                elif index == 4:
                    raise Exception("TOO MANY VALUES")
        else:
            for key, date in kwargs.items():
                if key == "id":
                    self.id = date
                elif key == "size":
                    self.size = date
                elif key == "x":
                    self.x = date
                elif key == "y":
                    self.y = date

    def to_dictionary(self):
        """ returns the dic representation of a Square """
        tmp = dict()
        tmp["id"] = self.id
        tmp["size"] = self.size
        tmp["x"] = self.x
        tmp["y"] = self.y
        return tmp
