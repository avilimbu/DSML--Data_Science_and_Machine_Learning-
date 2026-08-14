# Verify that A @ np.linalg.inv(A) produces an identity matrix.

import numpy as np

# Define a square matrix A
A = np.array([[4, 7], [2, 6]])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

# Verify that A @ A_inv produces an identity matrix
identity_matrix = A @ A_inv
print("A @ np.linalg.inv(A):")
print(identity_matrix)