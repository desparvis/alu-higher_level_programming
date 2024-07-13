#!/usr/bin/python3
"""
defining inherits_from
"""


def inherits_from(obj, a_class):
    """
    defines function inherits
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
