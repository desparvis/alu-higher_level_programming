#!/usr/bin/python3
def uniq_add(my_list=[]):
    uset = set()
    for num in my_list:
        uset.add(num)
        sum = sum(uset)
    return sum
