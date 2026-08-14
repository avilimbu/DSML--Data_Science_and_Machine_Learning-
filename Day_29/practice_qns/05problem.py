# Find the dot product of two vectors.

import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [7, 8],
    [9, 10],
    [11, 12]])

# Calculate the dot product
dot_product = np.dot(a, b)
print("Dot product of a and b:")
print(dot_product)