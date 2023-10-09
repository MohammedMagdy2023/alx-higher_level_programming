#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # make sure the tuples have at least 2 elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    # Add the first two elements of each tuple
    idx_1 = tuple_a[0] + tuple_b[0]
    idx_2 = tuple_a[1] + tuple_b[1]
    res = (idx_1, idx_2)
    return res
