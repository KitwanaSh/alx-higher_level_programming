#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints the first and last name.

    Arguments:
    @firstname: the first string to enter;
    @last_name: the second string to eneter.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
