#!/usr/bin/python3
"""
This module defines class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """"Initialization of the Square instance

        Attributes:
            width(int): The width of the Square
            height(int):The height of the Square
            x(int): the x coordinate of Square
            y(int): they coordinate of Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Setter method for size (width and height)"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """The string representation of square instance"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """
        updates the attributes of the  Rectangle instance

        Arguments:
            1st Argument: id attribute
            2nd Argument: size
            3rd Argument: x
            4th Argument: y
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self,  key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
