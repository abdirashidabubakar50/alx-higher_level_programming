#!/usr/bin/python3
"""
This module defines a function that returns True if the object
is an instance of a class that inherited(directly or indirectly) from
the specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
    True if obj is an instance of a class that inherited
    from _class, Otherwise False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
