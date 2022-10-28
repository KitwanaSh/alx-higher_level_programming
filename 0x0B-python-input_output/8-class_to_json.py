#!/usr/bin/python3

"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return a dictionary of a simple data structure form an object."""
    return obj.__dict__
