import numpy as np

# matrix_path
def matrix_path(matrix, i, j):
    """
    Matrix Path using Recursion
    matrix: 2nd-array numpy
    """
    if i == 0 and j == 0:
        return matrix[0, 0]
    elif i == 0:
        return matrix[0, j] + matrix_path(matrix, 0, j-1)
    elif j == 0:
        return matrix[i, 0] + matrix_path(matrix, i-1, 0)
    else:
        return matrix[i, j] + max(matrix_path(matrix, i-1, j), matrix_path(matrix, i, j-1))
    
def matrix_path_dp(matrix, i, j):
    """
    Matrix Path using Dynamic Programming
    matrix: 2nd-array numpy
    """
    path_matrix = np.zeros(matrix.shape)
    path_matrix[0, 0] = matrix[0, 0]
    row_size = matrix.shape[0]
    col_size = matrix.shape[1]
    for ii in range(1, row_size):
        path_matrix[ii, 0] = matrix[ii, 0] + path_matrix[ii-1, 0]
    for jj in range(1, col_size):
        path_matrix[0, jj] = matrix[0, jj] + path_matrix[0, jj-1]
    for ii in range(1, row_size):
        for jj in range(1, col_size):
            path_matrix[ii, jj] = matrix[ii, jj] + max(path_matrix[ii-1, jj], path_matrix[ii, jj-1])
    return path_matrix[i, j]