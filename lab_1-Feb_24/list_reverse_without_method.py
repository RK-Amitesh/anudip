# Problem 57
# Reverse a list without using reverse() method

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Create empty list to store reversed elements
reversed_list = []

# Loop from last index to first
for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

# Print result
print("Reversed list:", reversed_list)