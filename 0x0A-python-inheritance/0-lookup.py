#!/usr/bin/python3
"""
ffunction that returns the list of
available attributes and methods of an object
"""


def lookup(obj):
    """ function to return list of attributes and methodes"""
    return dir(obj)
