# Problem 75
# Find symmetric difference of two sets

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Find symmetric difference
result = set1.symmetric_difference(set2)

print("Symmetric Difference:", result)