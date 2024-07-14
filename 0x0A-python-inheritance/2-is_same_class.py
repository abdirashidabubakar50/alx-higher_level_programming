#!/usr/bin/python3
"""This module defines a function that returns True if
the object is exactly the instance of the specified class; otherwise
return False
"""

def is_same_class(obj, a_class):
    """Returns True if the object is exactly an isntance of the specified class, 
    otherwise false

    Args:
    obj: The object to check
    a_class: The class to check against

    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class