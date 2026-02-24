# Problem 61
# Rotate a list by K positions (Right Rotation)

# Taking list input
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Taking value of K
k = int(input("Enter number of positions to rotate: "))

# Get length of list
n = len(numbers)

# Handle cases where k > n
k = k % n
# This prevents unnecessary full rotations

# Perform rotation
rotated_list = numbers[-k:] + numbers[:-k]

# Print result
print("Rotated list:", rotated_list)