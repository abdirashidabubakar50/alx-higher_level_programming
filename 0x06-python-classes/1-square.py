#!/usr/bin/python3
"""
This module defines a class 'Square'

"""


class Square:
    """
    This class defines a square by its size

    Attributes:
        __size (int): The size of the square (private)
    """
    def __init__(self, size):
        """
        initializes a new instance of the Square class.

        Args:
            size (int): The size of the square
        """
        self.__size = size
