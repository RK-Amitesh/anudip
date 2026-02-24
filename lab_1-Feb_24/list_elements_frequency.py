# Problem 56
# Count frequency of elements in list (Basic Method)

# Taking input from user
user_input = input("Enter list elements separated by space: ")

# Convert input into list of integers
numbers = list(map(int, user_input.split()))

# Create empty list to track visited elements
visited = []

# Loop through list
for num in numbers:
    if num not in visited:
        count = 0

        # Count occurrences of num
        for item in numbers:
            if item == num:
                count += 1

        print(num, "appears", count, "times")
        visited.append(num)