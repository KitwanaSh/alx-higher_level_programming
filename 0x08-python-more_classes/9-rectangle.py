#!/usr/bin/python3
"""
The rectangle class
"""


class Rectangle():
    """ The rectangle class that includes
    - private attributes: width and height
    - public attributes: number_of_instances and print_symbol
    - static method: bigger_or_equal
    - puplic method: square
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initilalize the class with private attributes
        Args:
            width: int - private attribute
            height: int- private attribute
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Retrive the width attribute """
        return self.__width

    @property
    def height(self):
        """ Retrieve the height attribute """
        return self.__height

    @width.setter
    def width(self, value):
        """ Set the value of the width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """ Set the value of the height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Return the rare of the triangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Return  the perimeter of the triangle """
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return 2 * (self.__height + self.__height)

    def __str__(self):
        """ Print the attribute in string usign the  '#' """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = []
            for i in range(self.__height):
                for j in range(self.__width):
                    rect.append(str(Self.print_symbol))
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))

    def __repr__(self):
        """ Make a copy of the string representation """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """ When one of the intances of the Rectangle is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ check if rect_1 is bigger than rect_2 """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """ Return the new Rectangle intance """
        return (cls(size, size))
