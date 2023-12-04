#!/usr/bin/python3
def multiple_returns(sentence):
    temp = ()
    if len(sentence) == 0:
        temp = 0, "None"
    else:
        temp = len(sentence), sentence[0]
    return temp
