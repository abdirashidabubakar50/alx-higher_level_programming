#!/usr/bin/python3
""" This module defines class Square that inherits from class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a Square instance with size.

        Args:
            size(int): The size of the Square

        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the Square
        """
        return self.__size * self.__size
    
    def __str__(self):
        """Returns a string representation of the square instance"""
        return "[Square] {}/{}".format(self.__size, self.__size)