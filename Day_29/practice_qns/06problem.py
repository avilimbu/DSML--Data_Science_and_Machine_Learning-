# Find the cross product of two 3D vectors.

import numpy as np

# Define two 3D vectors

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [7, 8, 9],
    [10, 11, 12],])

# Calculate the cross product
cross_product = np.cross(a, b)
print("Cross product of a and b:")  
print(cross_product)

