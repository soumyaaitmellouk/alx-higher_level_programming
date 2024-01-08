#!/usr/bin/python3"""
"""
function to return a type
"""


def inherits_from(obj, a_class):
    """
    function to return a type
    :param obj: parameter 1
    :param a_class: parameter 2
    :return: True or False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
