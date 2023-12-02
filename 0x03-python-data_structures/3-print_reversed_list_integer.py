#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    r = -1
    while (r >= -len(my_list)):
        print("{:d}".format(my_list[r]))
        r = r - 1
