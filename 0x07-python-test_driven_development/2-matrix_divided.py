#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides a matrix by a number (float/int)
    - div must not be equal to '0'
    - each row of the matrix must be of the same size

    Arguments:
    @matrix: the list of lists
    @div: the divisor
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(each_row, list) for each_row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [list1 for each_row in matrix for list1 in each_row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(each_row) == len(matrix[0]) for each_row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")


    return ([list(map(lambda list1: round(list1 / div, 2), each_row)) for each_row in matrix])
