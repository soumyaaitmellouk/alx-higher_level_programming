#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(0, 3):
        for i in range(0, 3):
            print("{:d}".format(matrix[j][i]), end=" ")

        print()
