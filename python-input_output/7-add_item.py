#!/usr/bin/python3
"""
module needs documenting
"""


from sys import argv
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file.py").load_from_json_file
filename = "add_item.json"
json_list = load_from_json_file(filename)
for i in argv[:1]:
    json_list.append(i)
save_to_json_file(json_list, filename)
