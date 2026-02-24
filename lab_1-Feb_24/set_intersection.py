# Problem 72
# Perform intersection of two sets

# Take first set input from user
set1 = set(map(int, input("Enter first set elements separated by space: ").split()))
# split() → converts input into list of strings
# map(int, ...) → converts each element into integer
# set() → removes duplicates and creates a set

# Take second set input
set2 = set(map(int, input("Enter second set elements separated by space: ").split()))

# Find intersection (common elements)
result = set1.intersection(set2)

# Print result
print("Intersection of sets:", result)