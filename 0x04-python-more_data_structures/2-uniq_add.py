#!/usr/bin/python
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    addition = 0
    for element in new_list:
        addition += element
    return addition
