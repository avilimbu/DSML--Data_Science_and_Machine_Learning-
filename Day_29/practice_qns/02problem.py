# Solve a system of linear equations using np.linalg.solve().
# Ax = b, where A is the coefficient matrix and b is the constants vector.

import numpy as np
A = np.array([[3, 1], [1, 2]])

# Constants vector
b = np.array([9, 8])

# Solve the system
x = np.linalg.solve(A, b)

print("Solution:")
print(x)