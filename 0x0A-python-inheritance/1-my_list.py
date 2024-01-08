#!/usr/bin/python3
""" inheratance classes"""


class MyList(list):
    """
    print sorted list of a father class
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
