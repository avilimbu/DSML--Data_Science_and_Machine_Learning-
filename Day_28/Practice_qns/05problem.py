# Create a 4×4 identity matrix | Find the rank of a given matrix.

import numpy as np
identity_matrix = np.eye(4, dtype=int)
print(identity_matrix)

# finding the rank of a given matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank = np.linalg.matrix_rank(matrix)
print("Matrix:")
print(matrix)
print("Rank:")
print(rank)