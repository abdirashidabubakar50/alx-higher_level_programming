#!/usr/bin/python3
"""
This module defines a class Student
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates the Student class

        Args:
            first_name: The first name of the student
            last_name: The last name of the student
            age: The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student Instance
        """
        if attrs is None:
            return self.__dict__
        else:
            for attr in attrs:
                if attr in self.__dict__:
                    return {attr: self.__dict__[attr]}
