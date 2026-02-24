# Problem 58
# Merge two lists and remove duplicates (order preserved)

# Taking first list input
list1 = list(map(int, input("Enter elements of first list: ").split()))

# Taking second list input
list2 = list(map(int, input("Enter elements of second list: ").split()))

# Merge both lists
merged_list = list1 + list2

# Create empty list for unique elements
unique_list = []

# Loop through merged list
for item in merged_list:
    if item not in unique_list:
        unique_list.append(item)

# Print result
print("Merged list without duplicates:", unique_list)