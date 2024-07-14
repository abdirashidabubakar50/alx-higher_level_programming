#!/usr/bin/python3
"""This module defines a class that inherits from list
"""


class MyList(list):
    """This class has a public instance method that prints the list, 
     but sorted in ascending order """

    def print_sorted(self):
        """A public instance method that prints a list in ascending order"""
        print(sorted(self))
