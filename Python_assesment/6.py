# Q6. Write a Python program to merge two lists,
# remove duplicate values, sort the final list
# in descending order, and display only those
# numbers that are divisible by both 3 and 5.

list1 = []
list2 = []

n1 = int(input("Enter number of elements in List 1 : "))

for i in range(n1):

    value = int(input("Enter element : "))
    list1.append(value)

n2 = int(input("\nEnter number of elements in List 2 : "))

for i in range(n2):

    value = int(input("Enter element : "))
    list2.append(value)

# merging lists
merged_list = list1 + list2

# removing duplicates
final_list = list(set(merged_list))

# sorting in descending order
final_list.sort(reverse=True)

print("\nFinal List :", final_list)

print("\nNumbers divisible by both 3 and 5 are :")

for i in final_list:

    if i % 3 == 0 and i % 5 == 0:
        print(i)