#!/usr/bin/python3
"""class Rectangle"""
from base import Base


class Rectangle(Base):
    """
    represent a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialisation of parameters
        :param width: parameter 1
        :param height: parameter 2
        :param x: parameter 3
        :param y: parameter 4
        :param id: parameter 5
        """
        __width = width
        __height = height
        __x = x
        __y = y
        super().__init__(id)
