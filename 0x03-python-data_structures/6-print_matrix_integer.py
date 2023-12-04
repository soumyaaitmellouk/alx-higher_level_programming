#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == []:
        print("")
    else:
        for j in range(len(matrix)):
            for i in range(len(matrix[j])):
                print("{}".format(matrix[j][i]), end=" ")
            print()
