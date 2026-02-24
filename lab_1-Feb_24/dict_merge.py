# Problem 78
# Merge two dictionaries manually

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {}

# Add elements from dict1
for key in dict1:
    merged_dict[key] = dict1[key]

# Add elements from dict2
for key in dict2:
    merged_dict[key] = dict2[key]

print("Merged Dictionary:", merged_dict)