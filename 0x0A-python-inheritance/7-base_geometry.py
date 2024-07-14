#!/usr/bin/python3
"""
This module defines a BaseGeometry class with a public instance method area
and another public instance method integer_validator that validates value
"""

class BaseGeometry:
    """
    BaseGeometry class with a public instance method area.
    """ 
    def area(self):
        """
            Raises an Exception with  the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
