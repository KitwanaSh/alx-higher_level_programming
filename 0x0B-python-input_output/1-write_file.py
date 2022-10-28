#!/usr/bin/python3
"""Write a string to text file and print it number of characters"""


def write_file(filename="", text=""):
    """Prints the number of characters in a writen file
    
    Args:
        filename: the name of the writen file.
        text: The string to be writen.
    """
    with open(filename, mode='w', encoding='utf-8') as file_n:
        return file_n.write(text)
