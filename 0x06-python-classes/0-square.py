#!/usr/bin/python3
"""
This is module defines a class 'Square' which represents a square
with a given height and width

"""

class Square:
    """
    This is a class that defines a square by its height
    and width 

    Attributes:
        height (int): The height of the square. Defaults to 0
        widht (int): The width of the square. Defaults to 0
    """

    def __init__(self, height=0, width=0):
        """
        Initializes a new instance of the Square class.

        Args:
            height (int): The height of the square. Defautls to 0
            width (int): The width of the square. Defaults to 0
        """
        self.height = height
        self.width = width
