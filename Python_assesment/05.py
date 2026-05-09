# Q5. Design a Python function that accepts a list of integers
# and returns the second largest and second smallest element
# without using built-in sorting functions.

def find_numbers(list1):

    largest = second_largest = list1[0]
    smallest = second_smallest = list1[0]

    # finding largest and smallest
    for i in list1:

        if i > largest:
            second_largest = largest
            largest = i

        elif i > second_largest and i != largest:
            second_largest = i

        if i < smallest:
            second_smallest = smallest
            smallest = i

        elif i < second_smallest and i != smallest:
            second_smallest = i

    print("Second Largest Number =", second_largest)
    print("Second Smallest Number =", second_smallest)


# taking list input
numbers = []

n = int(input("How many numbers you want to enter : "))

for i in range(n):

    value = int(input("Enter number : "))
    numbers.append(value)

find_numbers(numbers)