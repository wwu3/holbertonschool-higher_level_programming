#!/usr/bin/python3
def safe_print_division(a, b):
    insideresult = None
    try:
        insideresult = a / b
    except ZeroDivisionError as e:
        print("", end='')
    finally:
        print("Inside result: {}".format(insideresult))
        return insideresult
