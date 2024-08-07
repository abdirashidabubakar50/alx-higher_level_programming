#!/usr/bin/python3
"""
This module defines a function that returns an object(Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    returns an object(Python data structure)
    represented by a JSON string

    Args:
        my_str: The JSON string to be deserialized

    Returns:
        object: The Python object represented by the JSOn string
    """
    return json.loads(my_str)
