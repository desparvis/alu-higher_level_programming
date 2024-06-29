#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return 
    reverse = my_list[::-1]

    for num in reverse:
        print("{:d}".format(num))
