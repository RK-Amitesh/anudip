# Problem 74
# Check whether one set is subset of another

set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Check subset condition
if set1.issubset(set2):
    print("Set1 is a subset of Set2.")
else:
    print("Set1 is NOT a subset of Set2.")