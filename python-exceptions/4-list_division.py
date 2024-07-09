#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in my range(list_length):
        try:
            if i >= len(my_list_1) or i>= len(my_list_2):
                raise IndexError("out of range")
            resu = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            resu = 0
        except ZeroDivisionError:
            print("division by 0")
            resu = 0
        except IndexError:
            print("out of range")
            resu = 0
        finally:
            result.append(resu)
    return result
