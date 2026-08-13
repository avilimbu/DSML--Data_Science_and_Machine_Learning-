# Find eigenvalues and eigenvectors of a 2×2 matrix.

import numpy as np
matrix = np.array([[4, -2], [1, 1]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Matrix:")
print(matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)