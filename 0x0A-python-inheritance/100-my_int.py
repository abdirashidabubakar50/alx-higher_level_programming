#!/usr/bin/python3
""" This module defines a class MyInt that inherits from int"""


class MyInt(int):
    """
    Myint is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """
        override the equality operator (==) to behave as inequality (!=)
        """
        return int(self) != other
    
    def __ne__(self, other):
        """
        override the inequality operator (!=) to behave as equality (==)
        """
        return int(self) == other\
