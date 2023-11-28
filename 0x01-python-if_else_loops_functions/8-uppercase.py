#!/usr/bin/python3
def uppercase(str):
    for char in str:
        uppChar = char
        if ord(uppChar) >= 97 and ord(uppChar) <= 122:
            uppChar = chr(ord(char) - 32)
        print("{}".format(uppChar), end="")
    print()
