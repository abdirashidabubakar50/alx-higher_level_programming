#!/usr/bin/python3
def no_c(my_string):
    no_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            no_string += char
    return no_string
