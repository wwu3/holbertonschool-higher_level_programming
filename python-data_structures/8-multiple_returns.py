#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == () and sentence =="":
        sentence[0] = None
        return (None)
    else:
        return (len(sentence), sentence[0])
