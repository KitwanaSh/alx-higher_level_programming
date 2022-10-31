#!/usr/bin/python3
""" Module that has class Square, inherictance or Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the instcances """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the __str__ method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_x_by_y = "{}/{} - ".format(self.x, self.y)
        str_w_by_h = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_x_by_y + str_w_by_h

    @property
    def size(self):
        """ getter sie """
        return self.width

    @size.setter
    def size(self, value):
        """ setter size """
        self.width = value
        self.height = value

    def __str(self):
        """ str special method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_x_by_y = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_squalre + str_id + str_x_by_y + str_size

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_attr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_attr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
