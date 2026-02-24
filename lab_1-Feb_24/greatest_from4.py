# Problem 20
# Find the greatest of four numbers

# Taking input from user
a = float(input("Enter first number: "))
# Convert input to float and store in 'a'

b = float(input("Enter second number: "))
# Convert input to float and store in 'b'

c = float(input("Enter third number: "))
# Convert input to float and store in 'c'

d = float(input("Enter fourth number: "))
# Convert input to float and store in 'd'

# Checking which number is greatest

if a >= b and a >= c and a >= d:
    # Check if 'a' is greater than or equal to all others
    greatest = a

elif b >= a and b >= c and b >= d:
    # Check if 'b' is greatest
    greatest = b

elif c >= a and c >= b and c >= d:
    # Check if 'c' is greatest
    greatest = c

else:
    # If none of the above, then 'd' must be greatest
    greatest = d

# Printing the result
print("The greatest number is:", greatest)