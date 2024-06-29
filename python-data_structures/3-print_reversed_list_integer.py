#!/usr/bin/python3
def print_reversed_integer(my_list=[]):
    reverse = my_list[::-1]

    for num in my_list:
        print("{:d}".format(num))
