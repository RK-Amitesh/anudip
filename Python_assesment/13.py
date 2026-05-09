# Q13. Write a NumPy program to create a 5x5 matrix
# with random integers and calculate row-wise sum,
# column-wise sum, transpose, and determinant.

import numpy as np

# creating 5x5 matrix
matrix = np.random.randint(1, 10, (5, 5))

print("Original Matrix :\n")
print(matrix)

# row-wise sum
print("\nRow-wise Sum :")
print(matrix.sum(axis=1))

# column-wise sum
print("\nColumn-wise Sum :")
print(matrix.sum(axis=0))

# transpose
print("\nTranspose of Matrix :")
print(matrix.T)

# determinant
print("\nDeterminant of Matrix :")
print(np.linalg.det(matrix))