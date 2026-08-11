# Declare a new array with contents [5,4,3,2,1] and slice it to select the last 3 items.

import numpy as np

arr = np.array([5,4,3,2,1])
result = arr[2:]

print(result) # [3 2 1]