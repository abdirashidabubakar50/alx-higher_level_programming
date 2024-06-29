#!/usr/bin/python3
"""
This module  defines a 'Square' class  with a private
instance attribute 'size'
"""


class Square:
    """
    This clas defines a square by its size.

    Attributes:
        __size (int): The size of the square (private)

    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if the size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
