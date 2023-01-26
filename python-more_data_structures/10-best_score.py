#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    biggest_key = list(a_dictionary)[0]
    biggest_value = a_dictionary[biggest_key]
    for key, value in a_dictionary.items():
        if value > biggest_value:
            biggest_key = key
            biggest_value = value
    return biggest_key
