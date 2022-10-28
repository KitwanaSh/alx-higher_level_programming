#!/usr/bin/python3
"""Reads a text file in the  UTF-8 encoding"""


def read_file(filename=""):
    """Read file using the 'with statement'

    Args:
        read_file(The function): tu read the file
        filename (argument): The variable for the file
    """
    with open(filename, encoding = 'utf-8') as file_n:
        print(file_n.read(),  end="")
