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
