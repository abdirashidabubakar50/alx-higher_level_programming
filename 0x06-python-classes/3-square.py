#!/usr/bin/python3
"""
This module defines a class 'Square' with a private
instance attribute 'size'
"""


class Square:
    """
     This class defines square by its size

     Attributes:
      __size: The size of the square (private)
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the self class

        Args:
            size (int): The size of the square

        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        """
        Computes the Area of the square.

        Returns:
             int: The Area of the square
        """
        return (self.__size * self.__size)
