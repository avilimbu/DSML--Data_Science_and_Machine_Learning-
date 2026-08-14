# Perform SVD on a 3×3 matrix and print U, S, and VT.

import numpy as np
# Define a 3x3 matrix   
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform Singular Value Decomposition
U, S, VT = np.linalg.svd(A)

print("U:")
print(U)
print("S:")
print(S)
print("VT:")
print(VT)