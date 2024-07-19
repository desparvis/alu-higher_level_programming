#!/usr/bin/python3
"""
module is well documented
"""


def append_write(filename="", text=""):
    """
    function is well documented
    """
    with open(filename, "a", encoding="utf-8"):
        result = file.write(text)
    return result
