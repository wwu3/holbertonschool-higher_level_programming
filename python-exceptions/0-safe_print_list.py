#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbers = 0
    try:
        for e in range(x):
            print("{}".format(my_list[e]), end='')
            numbers = numbers + 1
    except Exception:
        print("", end='')
    print()
    return numbers
