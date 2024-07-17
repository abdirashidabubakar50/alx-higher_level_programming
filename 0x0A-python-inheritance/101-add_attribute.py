#!/usr/bin/python3
"""
This module defines a function that add a new
attribute to an object if it's possible
"""


def add_attribute(obj, name, value):
    """
    This function adds a new attribute to an object if it's possible

    Args:
        obj: The object to which the attribute should be added
        name: the name of the attribute to add
        value: The value of the attribute to add.

    Raises:
        TypeError: if the object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
