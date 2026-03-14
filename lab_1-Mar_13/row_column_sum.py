# Q6
# Calculate row-wise and column-wise sum

import numpy as np

matrix = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

print("Row Sum:", matrix.sum(axis=1))
print("Column Sum:", matrix.sum(axis=0))

# Output
# Row Sum: [10 26 42 58]
# Column Sum: [28 32 36 40]