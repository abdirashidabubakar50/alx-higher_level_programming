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

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self, value):
        """Setter for the position attribute"""
        for num in value:
            if not isinstance(value, tuple):
                raise TypeError("position must be a tuple of 2 postive integers")
            if len(value) != 2:
                raise TypeError("postion must be a tuple of 2 postitive integers")
            if not all(isinstance(num, int)) and num>= 0:
                raise TypeError("poistion must be a tuple of 2 positive integers")
        self.__position = value
    def area(self):

        """
        Computes the Area of the square.

        Returns:
             int: The Area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints the square with the character #.
        If the size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
