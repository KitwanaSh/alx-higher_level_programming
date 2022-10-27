#!/usr/bin/python3

"""Define if something is kindof a class"""


def is_kind_of_class(obj, a_class):
    """Ckeck if an object is an instance or inheritance of a class

    Args:
        obj: The object ot chck
        a_class: The class to fit the type of object to

    """
    if isinstance(obj, a_class):
        return True
    return False
