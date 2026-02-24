# Problem 66
# Check if list is palindrome

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Reverse the list using slicing
reversed_list = numbers[::-1]

# Compare original and reversed list
if numbers == reversed_list:
    print("The list is a Palindrome.")
else:
    print("The list is NOT a Palindrome.")