def pascal_triangle(n):
    """ pascal triangle implementation
    """
    if n<=0:
        return []
    pascalTriangle = [[1]]
    for i in range(n-1):
        temp = [0]+pascalTriangle[-1]+[0]
        arr = []
        for j in range(len(temp) -1):
            arr.append(temp[j]+temp[j+1])
        pascalTriangle.append(arr)
    return pascalTriangle
