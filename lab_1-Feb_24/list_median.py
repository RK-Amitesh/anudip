# Problem 64
# Find median of a list

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Check if list is empty
if len(numbers) == 0:
    print("List is empty. Cannot find median.")

else:
    # Sort the list
    numbers.sort()

    n = len(numbers)

    # If number of elements is odd
    if n % 2 != 0:
        median = numbers[n // 2]

    # If number of elements is even
    else:
        middle1 = numbers[n // 2 - 1]
        middle2 = numbers[n // 2]
        median = (middle1 + middle2) / 2

    print("Median is:", median)