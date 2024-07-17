#!/usr/bin/python3
"""
This module defines a function that appends a string at the end of a text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of the text file
    and returns the number of characters added

    Args:
        filename: The name of the text file to append the string
        text: The string to append to the  text file
    """
    with open(filename, mode='a', encoding="utf-8") as File:
        new_content = File.write(text)
    return new_content
