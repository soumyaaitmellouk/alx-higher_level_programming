#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    temp = list(a_dictionary.keys())
    temp.sort()
    for i in temp
        print("{}: {}".format(i, a_dictionary.get(i)))
