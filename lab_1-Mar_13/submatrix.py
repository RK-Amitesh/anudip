# Q5
# Create array from 1 to 25 and extract middle 3x3 matrix

import numpy as np

arr = np.arange(1,26).reshape(5,5)

sub = arr[1:4,1:4]

print(sub)

# Output
# [[ 7  8  9]
#  [12 13 14]
#  [17 18 19]]