# Problem 73
# Perform difference of two sets

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Find difference
result = set1.difference(set2)

# Print result
print("Difference (set1 - set2):", result)