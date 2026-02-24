# Problem 62
# Find sum of list elements

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Initialize sum variable
total_sum = 0

# Loop through list elements
for num in numbers:
    total_sum += num
    # Same as: total_sum = total_sum + num

# Print result
print("Sum of list elements is:", total_sum)