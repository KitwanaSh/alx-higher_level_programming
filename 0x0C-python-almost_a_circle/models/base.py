#!/usr/bin/python3
""" Module with class Base """
import json
import csv
import os.path


class Base:
    """ The class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
           self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ List to json string """
        if list_of_dict is None or list_of_dict == "[]":
            return "[]"
        return json.dumps(list_of_dict)
