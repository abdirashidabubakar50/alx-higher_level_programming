#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set()
    for element in set_1:
        for element_2 in set_2:
            if (element == element_2):
                set_3.add(element)
    return set_3
