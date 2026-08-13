# Calculate the determinant of a 2×2 matrix.

import numpy as np
matrix = np.array([[4, 2], [3, 1]])
determinant = np.linalg.det(matrix)
print("Matrix:")
print(matrix)
print("Determinant:")
print(determinant)