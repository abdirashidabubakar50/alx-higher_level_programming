#!/usr/bin/python3
"""
This module defines a function that returns the dictionary description
with simple data structure (lilst, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    returns the dictionary description
    with simple data structure (lilst, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
