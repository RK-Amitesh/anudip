# Q2
# Create a 5x5 matrix with random integers between 1 and 100
# and find the minimum and maximum values

import numpy as np

matrix = np.random.randint(1, 101, (5,5))

print("Matrix:")
print(matrix)

print("Minimum value:", matrix.min())
print("Maximum value:", matrix.max())

# Example Output
# Matrix:
# [[23 45 12 89 34]
#  [67 11 90 54 32]
#  [76 28 19 47 65]
#  [14 73 52 39 81]
#  [60 21 48 70 16]]
#
# Minimum value: 11
# Maximum value: 90