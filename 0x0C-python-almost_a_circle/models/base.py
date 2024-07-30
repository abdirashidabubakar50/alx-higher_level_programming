#!/usr/bin/python3
"""
This module defines a class Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            str: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls,  list_objs):
        """writes the JSON string representation of list_objs to a file

            Arguments:
                list_objs(list): A list of instances  that inherit from Base
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))
