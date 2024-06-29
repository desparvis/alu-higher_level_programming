#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedk = sorted(a_dictionary.keys())
    for key in sortedk:
        print("{}: {}".format(key, a_dictionary[key]))
