#!/usr/bin/python3
"""
This module defines a function that creates an Object from a JSON File
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file

    Args:
        filename(str): The name of the JSON File

    Returns:
        obj: The python object represented by teh JSON file
    """
    with  open(filename, encoding='utf-8') as File:
        return json.load(File)
