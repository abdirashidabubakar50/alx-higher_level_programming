#!/usr/bin/python3
"""
This module defines a class Base
"""


class Base:
    """
    Base class for  managing id attribute in all future classes.

    Attributes:
        __nb_objects(int): Private class attribute that keeps track of the
        the number of instances created without a specified id.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance

        Args:
            id(int, optional): The id for the instance. If None,
            an id is automatically assigned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects