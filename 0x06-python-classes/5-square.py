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
        self.__size = size

    @property
    def size(self):
        """to retrieve the size
        return: the size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
         to set value
        :param value: the size
        """
        if (type(value) == int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
         Public instance method that returns the current square area
        :return:
            the area of square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        that prints in stdout the square with the character #
        """
        if(self.__size == 0):
            print(" ")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print(" ")
