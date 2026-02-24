# Problem 32
# Find factorial using for loop

# Taking input from user
n = int(input("Enter a number: "))
# Convert input string to integer
# Store in variable 'n'

# Check for negative number
if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Initialize factorial variable
    factorial = 1
    # We start multiplication from 1

    # Using for loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Multiply factorial by current value of i
        factorial *= i
        # Same as: factorial = factorial * i

    # Print result
    print("Factorial of", n, "is", factorial)
    