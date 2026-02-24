# Problem 64
# Replace negative numbers with zero

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Loop through list using index
for i in range(len(numbers)):
    
    # Check if number is negative
    if numbers[i] < 0:
        numbers[i] = 0
        # Replace negative number with 0

# Print updated list
print("Updated list:", numbers)