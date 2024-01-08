#!/usr/bin/python3
"""
function to return a type
"""


def is_kind_of_class(obj, a_class):
    """
    function to return a type
    :param obj: parameter 1
    :param a_class: parameter 2
    :return: True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
