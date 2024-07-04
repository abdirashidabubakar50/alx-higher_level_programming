#!/usr/bin/python3
"""
This module defines a function that adds two integers

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first integer or float to add
        b: The second integer or float to add

    Returns:
        The sum of the two integers

    Raises:
        TypeError: if a or b are not integers or floats
    """

    if not isinstance(a,  (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
