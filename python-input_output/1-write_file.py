#!/usr/bin/python3
"""
module is well documented
"""


def write_file(filename="", text=""):
    """
    function is well documented
    """
    with open(filename, "w", encoding="utf-8") as file:
        result = file.write(text)
    return result
