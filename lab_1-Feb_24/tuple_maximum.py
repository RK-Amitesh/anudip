# Problem 67
# Flatten a nested list (one-level nesting)

# Example nested list
nested_list = [1, [2, 3], [4, 5], 6]

# Create empty list
flat_list = []

# Loop through elements
for item in nested_list:

    # If item is a list
    if isinstance(item, list):
        # Add each element inside nested list
        for sub_item in item:
            flat_list.append(sub_item)
    else:
        # If not list, add directly
        flat_list.append(item)

# Print result
print("Flattened list:", flat_list)