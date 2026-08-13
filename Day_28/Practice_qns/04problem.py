# Find the inverse of a matrix and verify the result.

import numpy as np
matrix = np.array([[4, 7], [2, 6]])
inverse_matrix = np.linalg.inv(matrix)
print("Original Matrix:")
print(matrix)
print("Inverse Matrix:")
print(inverse_matrix)
print("Verification (Original * Inverse):")
print(np.dot(matrix, inverse_matrix))