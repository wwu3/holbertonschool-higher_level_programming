#!/usr/bin/python3
def uniq_add(my_list=[]):
    results = 0
    for e in set(my_list):
        results = results + e
    return results
