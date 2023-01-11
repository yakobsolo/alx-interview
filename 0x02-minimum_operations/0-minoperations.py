#!/usr/bin/python3
"""
minimum operation
"""


def minOperations(n):
    """ returns minimum operation """
    nOpe = 0
    minOpe = 2
    while n > 1:
        while n % minOpe == 0:
            nOpe += minOpe
            n /= minOpe
        minOpe += 1
    return nOpe
