#!/usr/bin/python3
def divide(x, y):
    if x is None or y is None:
        print("out of range")
        return 0
    sum = 0
    try:
        sum = x / y
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    finally:
        return sum


def list_division(my_list_1, my_list_2, list_length):
    my_list_1 = my_list_1[:list_length]
    my_list_2 = my_list_2[:list_length]
    if my_list_1[0] == 0 or my_list_2[0] == 0:
        print("out of range")
    new_list = list()
    try:
        new_list = list(map(divide, my_list_1, my_list_2))
    except ZeroDivisionError:
        print("z", end='')
    except TypeError as e:
        print("t", end='')
    finally:
        return new_list
