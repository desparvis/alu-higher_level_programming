#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for elm in my_list:
        if elm == search:
            result.append(replace)
        else:
            result.append(elm)
    return result
