# Compute the trace of a matrix.

import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# The trace of a matrix is the sum of the elements on its main diagonal (from the top-left to the bottom-right).
trace = np.trace(matrix)
print("Matrix:")
print(matrix)
print("Trace:")
print(trace)