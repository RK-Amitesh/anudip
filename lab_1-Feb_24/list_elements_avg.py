# Problem 63
# Find average of list elements

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Check if list is empty
if len(numbers) == 0:
    print("List is empty. Cannot calculate average.")
else:
    total_sum = 0

    # Calculate sum manually
    for num in numbers:
        total_sum += num

    # Calculate average
    average = total_sum / len(numbers)

    # Print result
    print("Average of list elements is:", average)