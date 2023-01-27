#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for e in range(x):
        try:
            print("{:d}".format(my_list[e]), end='')
            number = number + 1
        except TypeError as e:
            print('', end='')
        except ValueError as e:
            print('', end='')
    print()
    return number
