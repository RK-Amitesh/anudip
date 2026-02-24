# Problem 55
# Find second largest number in list

# Taking input from user
user_input = input("Enter list elements separated by space: ")

# Convert input string into list of integers
numbers = list(map(int, user_input.split()))

# Remove duplicates to avoid repetition
numbers = list(set(numbers))

# Check if list has at least 2 unique elements
if len(numbers) < 2:
    print("Second largest element does not exist.")

else:
    # Assume first element is largest
    largest = numbers[0]
    second_largest = float('-inf')  # Very small number

    # Find largest number
    for num in numbers:
        if num > largest:
            largest = num

    # Find second largest
    for num in numbers:
        if num != largest and num > second_largest:
            second_largest = num

    print("Second largest element is:", second_largest)