#!/usr/bin/python3
""" Return True if all boxes can be opened, else return False """


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened. """
    leng = len(boxes)
    keyss = [0]
    for i in keyss:
        for j in boxes[i]:
            if j not in keyss:
                if j < leng:
                    myList.append(j)
    if len(keyss) == leng:
        return True
    return False
