# Problem 66
# Find maximum value in a tuple

# Taking input from user
numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Check if tuple is empty
if len(numbers) == 0:
    print("Tuple is empty.")
else:
    # Assume first element is maximum
    maximum = numbers[0]

    # Loop through tuple elements
    for num in numbers:
        if num > maximum:
            maximum = num
            # Update maximum if larger value found

    # Print result
    print("Maximum value:", maximum)