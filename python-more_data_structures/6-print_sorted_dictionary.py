#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for e, v in sorted(a_dictionary.items()):
        print("{}: {}".format(e, v))
