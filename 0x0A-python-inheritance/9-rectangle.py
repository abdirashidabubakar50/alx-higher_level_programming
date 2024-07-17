#!usr/bin/python3
""" This module defines a class Rectangle that inherits from
the the class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            with(int): The width of the rectangle
            height(int): The height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the
        the Rectangle instance
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
