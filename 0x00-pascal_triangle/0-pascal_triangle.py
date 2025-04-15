#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    result = []
    for i in range(n):
        if i == 0:
            current_row = [1]
        else:
            previous_row = result[i-1]
            current_row = [1]
            for j in range(1, len(previous_row)):
                current_row.append(previous_row[j-1] + previous_row[j])
            current_row.append(1)
        result.append(current_row)
    return result
