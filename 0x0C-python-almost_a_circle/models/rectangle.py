#!/usr/bin/python3
"""Models that have class Rectangle,
this is an inheritance of class Base
"""
from models.base import Base

class Rectangle(Base):
    """ Rectangle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Starts instances """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """ The area of the rectanle object """
        return self.width * self.height
