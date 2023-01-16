#!/usr/bin/python3
""" Finds peak of the class
    Args()
    - returns the biggest or second number
"""


def find_peak(list_of_integers):
    """ Find a peak in an unsorted list """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
