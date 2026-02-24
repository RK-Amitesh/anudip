# Problem 71
# Perform union of two sets

# Taking first set input
set1 = set(map(int, input("Enter elements of first set separated by space: ").split()))

# Taking second set input
set2 = set(map(int, input("Enter elements of second set separated by space: ").split()))

# Perform union
result = set1.union(set2)

# Print result
print("Union of sets:", result)