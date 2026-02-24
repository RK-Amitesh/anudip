# Problem 44
# Find maximum of three numbers using function

# Define function to find maximum
def find_max(a, b, c):
    
    # Check if 'a' is greater than or equal to both b and c
    if a >= b and a >= c:
        return a

    # Check if 'b' is greater than or equal to both a and c
    elif b >= a and b >= c:
        return b

    # Otherwise, 'c' must be the greatest
    else:
        return c


# Taking input from user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

# Call the function
maximum = find_max(x, y, z)

# Print result
print("The maximum number is:", maximum)