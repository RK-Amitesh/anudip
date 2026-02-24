# Problem 54
# Sort a list without using sort() method

# Taking input from user
user_input = input("Enter list elements separated by space: ")

# Convert input string into list of integers
numbers = list(map(int, user_input.split()))

# Get length of list
n = len(numbers)

# Bubble Sort Algorithm
for i in range(n):
    # Each pass places the largest element at the end
    
    for j in range(0, n - i - 1):
        # Compare adjacent elements
        
        if numbers[j] > numbers[j + 1]:
            # Swap if elements are in wrong order
            
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# Print sorted list
print("Sorted list:", numbers)