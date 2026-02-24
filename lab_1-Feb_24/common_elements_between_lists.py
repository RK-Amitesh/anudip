# Problem 60
# Find common elements between two lists

# Taking first list input
list1 = list(map(int, input("Enter elements of first list: ").split()))

# Taking second list input
list2 = list(map(int, input("Enter elements of second list: ").split()))

# Create empty list to store common elements
common_elements = []

# Loop through first list
for item in list1:
    # Check if item exists in second list
    # and avoid duplicates in result
    if item in list2 and item not in common_elements:
        common_elements.append(item)

# Print result
print("Common elements:", common_elements)