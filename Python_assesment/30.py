# Q30. Write a NumPy program to create two matrices
# and perform addition, subtraction, multiplication,
# and inverse operations.

import numpy as np

# creating matrices
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix 1 :\n")
print(matrix1)

print("\nMatrix 2 :\n")
print(matrix2)

# addition
print("\nAddition :\n")
print(matrix1 + matrix2)

# subtraction
print("\nSubtraction :\n")
print(matrix1 - matrix2)

# multiplication
print("\nMultiplication :\n")
print(np.dot(matrix1, matrix2))

# inverse of matrix1
print("\nInverse of Matrix 1 :\n")
print(np.linalg.inv(matrix1))