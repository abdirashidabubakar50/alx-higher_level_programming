#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file(UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as File:
        new_content = File.write(text)
    return new_content