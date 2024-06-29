#!/usr/bin/python3
def uniq_add(my_list=[]):
    usum = 0
    uset = set()
    for num in my_list:
        uset.add(num)
        usum = sum(uset)
    return usum
