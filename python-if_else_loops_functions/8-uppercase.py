#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        result += chr(ord(char) - 32) if ord('a') <= ord(char) <= ord('z') else char
    print("{}".format(result))
