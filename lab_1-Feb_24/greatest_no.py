# Problem 3
# Find the largest of three numbers

# Taking first number as input
a = int(input("Enter first number: "))
# Converts input to integer and stores in variable 'a'

# Taking second number as input
b = int(input("Enter second number: "))
# Converts input to integer and stores in variable 'b'

# Taking third number as input
c = int(input("Enter third number: "))
# Converts input to integer and stores in variable 'c'

# Checking conditions to find the largest number

if a >= b and a >= c:
    # This block executes if 'a' is greater than or equal to both b and c
    largest = a
    # Store 'a' in variable 'largest'

elif b >= a and b >= c:
    # This block executes if 'b' is greater than or equal to both a and c
    largest = b
    # Store 'b' in variable 'largest'

else:
    # If neither 'a' nor 'b' is the largest,
    # then 'c' must be the largest
    largest = c
    # Store 'c' in variable 'largest'

# Printing the result
print("The largest number is:", largest)