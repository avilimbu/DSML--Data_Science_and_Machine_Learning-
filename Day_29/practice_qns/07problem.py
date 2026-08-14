# Multiply two matrices using @.

import numpy as np

# Define two matrices
A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

# Multiply the matrices using @ operator
result = A @ B
print("Result of A @ B:")
print(result)


dot_product = np.dot(A, B)
print("Result of np.dot(A, B):")  
print(dot_product) 