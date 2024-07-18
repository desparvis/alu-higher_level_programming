#!/usr/bin/python3
"""
module is well  documented
"""


def read_file(filename=""):
    """
    function is well documented
    """
    with open(filename, 'r', encoding='utf-8'):
        result = file.read()
        print(result)
