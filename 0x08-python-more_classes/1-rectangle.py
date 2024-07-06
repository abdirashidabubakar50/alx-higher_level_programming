#!/usr/bin/python3
"""This module defines class Rectangle
"""


class Rectangle:
    """Defines a rectangle by its width and height with validation."""

    def __init__(self, width=0, height=0):
        """"Initializes a new instance of the rectangle9private
        Args:
            width: The width of the rectangle
        """
        self.__width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
