#!/usr/bin/python3
def add_integer(a, b=98):
    """The function that adds two integers

        Arguments:
        @a: first argument (integer)
        @b: second argumebr (integer), by default = 98
    """

    if type(a) not in[int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in[int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
