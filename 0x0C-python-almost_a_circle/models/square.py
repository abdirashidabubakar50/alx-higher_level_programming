#!/usr/bin/python3
"""
This module defines class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)
