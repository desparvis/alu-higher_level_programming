#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared = []
        for num in row:
            squared.append(num ** 2)
        result.append(squared)
    return result
