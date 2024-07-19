#!/usr/bin/python3
"""
module is well documented
"""


def def class_to_json(obj):
    """
    function is well documented
    """
    return {key: value for key, value in obj.__dict__.items()
            if isinstance(value, (list, dict, str, int, bool))}
