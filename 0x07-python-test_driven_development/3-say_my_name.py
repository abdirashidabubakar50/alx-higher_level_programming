#!/usr/bin/python3
"""
This module defines a function that prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """
    This is a function that prints first name and last name

    Args:
        first_name: first name of the person
        last_name: last name of the person

    Raises:
        TypeError: if first name or last name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
