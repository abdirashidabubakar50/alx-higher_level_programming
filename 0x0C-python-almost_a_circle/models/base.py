#!/usr/bin/python3
"""
This module defines a class Base
"""
import json
import os
import csv


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
        if list_dictionaries is None or not list_dictionaries:
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

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string  representation json_string
        """
        if json_string is None or json_string == "":
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + "csv"
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])
    
    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes CSV from a file and returns a list of instances

        Returns:
            list: A list of instances of the class
        """
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        instances = []
        with open(filename, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    id, width, height, x, y = map(int, row)
                    instances.append(cls.create(id=id, width=width, height=height,
                                                x=x, y=y))
                elif cls.__name__ == 'Square':
                    id, size, x, y = map(int, row)
                    instances.append(cls.create(id=id, size=size, x=x, y=y))
        return instances