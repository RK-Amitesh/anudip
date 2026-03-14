# Program: Generate Identity Matrices using NumPy
# Description:
# This program demonstrates how to create identity (unit) matrices
# using the NumPy library. It generates:
# 1. A 4x4 identity matrix
# 2. A 5x5 identity matrix with integer data type

# Import NumPy library
# NumPy is used for numerical computing and matrix operations
import numpy as np

# -------------------------------
# Creating a 4x4 Identity Matrix
# -------------------------------

# np.eye(n) generates an identity matrix of size n x n
# In an identity matrix:
# - All diagonal elements are 1
# - All other elements are 0
array = np.eye(4)

# Display the matrix
print("4x4 Identity Matrix:")
print(array)

# -----------------------------------------
# Creating a 5x5 Identity Matrix (Integer)
# -----------------------------------------

# By default, NumPy stores values as floating point numbers.
# dtype=int converts the matrix values into integers.
array2 = np.eye(5, dtype=int)

# Display the matrix
print("\n5x5 Identity Matrix (Integer Type):")
print(array2)

# Output
# 4x4 Identity Matrix:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
#
# 5x5 Identity Matrix (Integer Type):
# [[1 0 0 0 0]
#  [0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]