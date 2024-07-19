#!/usr/bin/python3
"""
document module importing json
"""
import json


def save_to_json_file(my_obj, filename) as a:
    """
    document function writing file using JSON
    """
    with open(filename, 'w', encoding="utf-8"):
        json.dump(my_obj, a)
        
