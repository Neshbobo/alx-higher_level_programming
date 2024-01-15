#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
"""Compute the square value of all integers in a matrix."""
result_matrix = []

for row in matrix:
result_row = []

for element in row:
result_row.append(element ** 2)

result_matrix.append(result_row)

return result_matrix
