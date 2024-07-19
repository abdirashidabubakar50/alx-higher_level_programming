#!/usr/bin/python3
"""
This module defines class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that  inherits from class Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of the Rectangle instance

        Attributes:
            width(int): The width of the Rectangle
            height(int):The height of the Rectangle
            x(int): the x coordinate of rectangle
            y(int): they coordinate of rectangle
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
