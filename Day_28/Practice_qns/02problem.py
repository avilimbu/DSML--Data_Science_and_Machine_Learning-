# Find the transpose of a 2×4 matrix.

import numpy as np
matrix = np.array([
[1, 2, 3, 4],
[5, 6, 7, 8]
])

transpose_matrix = matrix.T
print("Original Matrix:")   
print(matrix)
print("Transpose of the Matrix:")   
print(transpose_matrix)