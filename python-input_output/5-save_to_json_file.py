#!/usr/bin/python3
"""
module is well documented
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function is well documented
    """
    with open(filename, 'w' encoding="utf-8") as file:
        string = file.dumps(my_obj)
        file.write(stringi)
