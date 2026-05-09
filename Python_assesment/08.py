# Q8. Write a Python program to perform union,
# intersection, symmetric difference, and subset
# operations on two sets entered by the user.

set1 = set()
set2 = set()

n1 = int(input("Enter number of elements in Set 1 : "))

for i in range(n1):

    value = int(input("Enter element : "))
    set1.add(value)

n2 = int(input("\nEnter number of elements in Set 2 : "))

for i in range(n2):

    value = int(input("Enter element : "))
    set2.add(value)

# union
print("\nUnion =", set1.union(set2))

# intersection
print("Intersection =", set1.intersection(set2))

# symmetric difference
print("Symmetric Difference =",
    set1.symmetric_difference(set2))

# subset checking
if set1.issubset(set2):

    print("Set 1 is a subset of Set 2")

elif set2.issubset(set1):

    print("Set 2 is a subset of Set 1")

else:

    print("No set is a subset of another")