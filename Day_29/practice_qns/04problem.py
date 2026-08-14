# Calculate the norm of a vector.

import numpy as np
# Define a vector
v = np.array([3, 4])  # root of 3^2 + 4^2 = 5

# Calculate the norm (magnitude) of the vector
norm_v = np.linalg.norm(v)
print("Norm of the vector:")    
print(norm_v)