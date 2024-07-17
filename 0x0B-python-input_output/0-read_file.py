#!/usr/bin/python3
"""
This module defines a function that reads a test file(UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        content = f.read()
    print(content)
