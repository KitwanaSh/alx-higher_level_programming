#!/usr/bin/python3
def print_square(size):
    """Prints a square with the character '#'

    Argumens:
    @size: the size length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for n in range(size):
        for m in range(size):
            print("#", end="")
        print()
