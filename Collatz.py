#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

cache = {


}


def collatz_read(s):

    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    tests if the range i, j exists in the cache already from pre-determined values
    in a for loop, test each number x in the range i, j
    while x is not 1, it will continue to iterate through and add/divide/multiply
    if after a few cycles, "x" exists in the cache then add the cycle number (from cache) to current_length and move on
    eager cache -> if x does not exist in cache, add it
    once x reaches 1, if the current_length of the cycle is larger than the max_length then current becomes the new max
    """
    # assert (i >= 0 and j >= 0), "You cannot have negative values!"
    # assert (i != None  and j!= None), "You must enter 2 values!"
    # tested assertions but removed for final code

    if i > j:
        i,j = j, i
    max_length = 0


    if (i , j ) in cache:
            max_length = cache[(i, j)]
            return max_length

    for x in range(i, j + 1):
        current_length = 1

        while x > 1:
            if x in cache:
                current_length += cache[x]
                break
            else:
                if (x % 2) == 0:
                    x = (x // 2)
                else:
                    x = (3 * x) + 1
            current_length += 1

        if x not in cache:
            cache[x] = current_length

        if current_length > max_length:
            max_length = current_length

    return max_length

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
