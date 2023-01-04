#!/usr/bin/python3
"""
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    " 
    T.C O(n) 
    S.C O(n)
    "
    keys = []
    for box in boxes:
        keys+=box
    for i in range(len(boxes)):
        if i+1 not in keys:
            return False
    return True
