# Problem 49
# Return unique elements from a list using function

# Define function
def get_unique_elements(lst):

    # Initialize empty list to store unique elements
    unique_list = []

    # Loop through each element in input list
    for item in lst:

        # Check if item is not already in unique_list
        if item not in unique_list:
            unique_list.append(item)
            # Add item only if not present

    return unique_list


# Taking list input from user
# Example input format: 1 2 2 3 4 3 5
user_input = input("Enter list elements separated by space: ")

# Convert input string into list of integers
numbers = list(map(int, user_input.split()))

# Call function
result = get_unique_elements(numbers)

# Print result
print("Unique elements:", result)