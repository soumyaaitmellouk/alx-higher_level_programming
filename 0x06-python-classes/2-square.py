#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """class define a square"""
    def __init__(self, size=0):
        """
         Instantiate square  with a specified size

         Args:
             size (int): Size of the instance.
        """
        if (type(size) == int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        elif (type(size) == str):
            raise TypeError("size must be an integer")
