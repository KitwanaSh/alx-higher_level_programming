#!/usr/bin/python3
"""Appends a tring at the end of another string in a file"""


def append_write(filename="", text=""):
    """appends a to a string text file another string
    or write a new text if there is no file

    Args:
        filename (txt): A txt filename variable
        text (str): The string variable withe the text is to be appended

    """
    with open(filename, mode='a', encoding='utf-8') as file_n:
        return file_n.write(text)
