#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp = ()
    first = tuple_a + (0, 0)
    seconde = tuple_b + (0, 0)
    temp = first[0] + seconde[0], first[1] + seconde[1]
    return temp
