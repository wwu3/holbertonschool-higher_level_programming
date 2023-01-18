#!/usr/bin/python3
def islower(c):
    for i in c:
        if i.islower():
            return True
        elif c == '':
            return False
        else:
            return False
