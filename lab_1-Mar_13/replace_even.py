# Q3
# Create array from 1 to 10
# Replace all even numbers with 0

import numpy as np

arr = np.arange(1, 11)

# Replace even numbers
arr[arr % 2 == 0] = 0

print(arr)

# Output
# [1 0 3 0 5 0 7 0 9 0]