#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted = sorted(a_dictionary())
    for key in sorted:
        print("{}: {}".format(key, a_dictionary[key]))
