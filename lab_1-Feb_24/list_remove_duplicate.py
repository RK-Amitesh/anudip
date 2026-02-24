# Problem 53
# Remove duplicate elements from list

# Taking input from user
user_input = input("Enter list elements separated by space: ")

# Convert input string into list of integers
numbers = list(map(int, user_input.split()))

# Initialize empty list to store unique elements
unique_list = []

# Loop through each element
for num in numbers:
    # Check if element is not already in unique_list
    if num not in unique_list:
        unique_list.append(num)
        # Add element only if it is not already present

# Print result
print("List after removing duplicates:", unique_list)