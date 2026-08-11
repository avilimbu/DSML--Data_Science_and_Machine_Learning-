# se arr as defined in 2.3. Exclude the last element from the list, but now only select
# every 3rd element. Remember the third index indicates stride

import numpy as np

arr = np.array([5,4,3,2,1])

result = arr[:-1:3]

print(result) # [5 2]