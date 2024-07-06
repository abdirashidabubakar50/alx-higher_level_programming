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
        self.width = width
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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of the rectangle

        Returns:
            int: the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Computes the perimeter of the rectangle

        Returns:
            int: Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Returns a string representation of the rectangle using the '#'
        character.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rect_lines = []
        for _ in range(self.height):
            rect_lines.append("#" * self.__width)
        
        return "\n".join(rect_lines)
