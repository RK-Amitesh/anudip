# Problem 67
# Find minimum value in a tuple

# Taking input from user
numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Check if tuple is empty
if len(numbers) == 0:
    print("Tuple is empty.")
else:
    # Assume first element is minimum
    minimum = numbers[0]

    # Loop through tuple elements
    for num in numbers:
        if num < minimum:
            minimum = num
            # Update minimum if smaller value found

    # Print result
    print("Minimum value:", minimum)