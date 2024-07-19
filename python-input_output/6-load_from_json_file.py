#!/usr/bin/python3
"""
well documented module
"""
import json


def load_from_json_file(filename):
    """
    well defined function
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
