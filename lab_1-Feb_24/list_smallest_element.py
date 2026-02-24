# Problem 52
# Find smallest element in a list

# Taking input from user
# Example input: 5 10 3 8 21
user_input = input("Enter list elements separated by space: ")

# Convert input string into list of integers
numbers = list(map(int, user_input.split()))

# Check if list is empty
if len(numbers) == 0:
    print("List is empty.")

else:
    # Assume first element is smallest
    smallest = numbers[0]

    # Loop through list elements
    for num in numbers:
        if num < smallest:
            smallest = num
            # Update smallest if smaller number found

    # Print result
    print("Smallest element is:", smallest)