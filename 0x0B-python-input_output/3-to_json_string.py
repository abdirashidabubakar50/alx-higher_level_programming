#!/usr/bin/python3
"""This module defines a function that returns the JSON representation
of an object(string):
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object(string)

    Args:
        my_obj: The object to be serialized to a JSON string
    """
    return json.dumps(my_obj)
