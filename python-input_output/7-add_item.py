#!/usr/bin/python3
"""
this module is well documenting
"""

from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file.py").load_from_json_file
filename = "add_item.json"
json_list = load(filename)
for i in argv[:1]:
    json_list.append(i)
save(json_list, filename)
