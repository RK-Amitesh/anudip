# Problem 15
# Check whether a number is divisible by both 3 and 5

# Taking input from user
num = int(input("Enter a number: "))
# Convert input string into integer
# Store in variable 'num'

# Checking divisibility condition
if num % 3 == 0 and num % 5 == 0:
    # % gives remainder
    # If remainder is 0 when divided by both 3 and 5
    # Then number is divisible by both
    print("The number is divisible by both 3 and 5.")

else:
    # If above condition is False
    print("The number is NOT divisible by both 3 and 5.")