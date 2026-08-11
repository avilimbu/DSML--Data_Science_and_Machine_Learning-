# You’ll need to combine array comparisons and logical operators to solve this one.
# Find out the values in the following array that are greater than 3 AND less than 7.
# The output should be a boolean array.

import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

result = (arr>3) & (arr<7)

for value, condition in zip(arr, result):
    print(f"{value} = {condition}")
    
    
# Output
# 1 = False
# 2 = False
# 3 = False
# 4 = True
# 5 = True
# 6 = True
# 7 = False
# 8 = False