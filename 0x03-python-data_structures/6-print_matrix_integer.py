#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(9):
        for j in range(3):
            print("{:d}".format(matrix[i][j]))
        print
