#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file(UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename: The name of the text file to write to
        text: The string to write to the text file
    """
    with open(filename, "w", encoding="utf-8") as File:
        new_content = File.write(text)
    return new_content
