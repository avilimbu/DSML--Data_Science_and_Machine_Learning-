# Find eigenvalues and eigenvectors of a 2×2 matrix.

import numpy as np
a = np.array([[4, 2], [1, 3]])

eigenvalues, eigenvectors = np.linalg.eig(a)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)