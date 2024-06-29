#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_i = my_list[0]
    for num in my_list:
        if num > max_i:
            max_i = num
    return max_i
