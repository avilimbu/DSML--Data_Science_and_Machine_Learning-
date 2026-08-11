# Select all the elements in the array below excluding the last one

import numpy as np

arr = np.array([5,4,3,2,1])
result = arr[:-1]

print(result) # [5 4 3 2]