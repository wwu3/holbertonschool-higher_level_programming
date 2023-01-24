#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    my_max = my_list[0]
    for e in my_list:
        if e > my_max:
            my_max = e
    return my_max
