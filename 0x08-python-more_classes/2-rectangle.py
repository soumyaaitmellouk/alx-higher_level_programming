#!/usr/bin/python3
"""Class Define a rectangle"""


class Rectangle:

    """ class define a rectagle"""

    def __init__(self, width=0, height=0):
        """
        initalize the attributes
        :param width: the width of rectangle
        :param height: the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        to retrieve the width
        :return: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
                to set value of width
                :param value: the width
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        else:
            if (value < 0):
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        set the height of rectangle
        :return: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
                 to set value of height
                :param value: the height
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        else:
            if (value < 0):
                raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        function to calculate the area of rectangle
        :return: the area
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        function to calculate the perimetr  of a rectangle
        :return: the perimeter
        """
        return (self.__width + self.__height) * 2
