#!/usr/bin/python3
''' Defines the function pascal_triangle(n) '''

def pascal_triangle(n):
    ''' returns a list of integers representing the Pascal's triangle of n '''
    if n <= 0:
        return []
    else:
        pascalTriangle = []
        for x in range(n):
            row = [1]
            if pascalTriangle:
                last_row = pascalTriangle[-1]
                row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
                row.append(1)
            pascalTriangle.append(row)
        return pascalTriangle
