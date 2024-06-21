#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for element_1 in set_1:
        for element_2 in set_2:
            if (element_1 not in set_2):
                set_3.add(element_1)
            if (element_2 not in set_1):
                set_3.add(element_2)
            # elif (element_2 != element_1):
            #     set_3.add(element_2)
    return set_3
