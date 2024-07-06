#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new
lines after each of these characters(. ? :)
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after
    each of these characters (. ? :)

    Args:
        text: the text string

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            i += 1
            # Skip any spaces following the punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end="")
