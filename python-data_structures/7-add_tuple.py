#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    a1, a2 = a[0], a[1]
    b1, b2 = b[0], b[1]
    sum = (a1 + b1, a2 + b2)
    return sum
