#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i=0
    count = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[num], int):
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
                i += 1
            except(ValueError, TypeError):
                continue
            except IndexError:
                break
    except:
        raise
    print()
    return count
