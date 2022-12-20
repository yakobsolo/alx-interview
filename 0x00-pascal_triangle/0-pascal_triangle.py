#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """ pascal triangle implementation
    arg:
        integer n
    return:
        list of lists
    """

<<<<<<< HEAD
    if n <= 0:
        return []

    pascalTriangle = [[1]]
=======
    pascalTriangle = [[1]]
        
    if n<=0:
        return []
    
>>>>>>> 9a33f3c3b0061bd034fc60cce43f4d23a0f839f8
    for i in range(n-1):
        temp = [0]+pascalTriangle[-1]+[0]
        arr = []
        for j in range(len(temp) - 1):
            arr.append(temp[j]+temp[j+1])
        pascalTriangle.append(arr)
        
    return pascalTriangle
