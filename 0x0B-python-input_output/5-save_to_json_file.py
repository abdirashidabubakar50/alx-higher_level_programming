#!/usr/bin/python3
"""
This module defines a function that writes an Object to a text file,
using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file,
    using JSON representation

    Args:
        my_obj: The object to be serialized and written to the file
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
