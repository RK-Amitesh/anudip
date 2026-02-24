# Problem 59
# Separate even and odd numbers from list

# Taking input from user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Create empty lists
even_list = []
odd_list = []

# Loop through numbers
for num in numbers:
    
    # Check if number is even
    if num % 2 == 0:
        even_list.append(num)
        # Add to even list
    
    else:
        odd_list.append(num)
        # Add to odd list

# Print results
print("Even numbers:", even_list)
print("Odd numbers:", odd_list)