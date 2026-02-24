# Problem 22
# Find factorial using while loop

# Taking input from user
n = int(input("Enter a number: "))
# Convert input string to integer
# Store in variable 'n'

# Check if number is negative
if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # Initialize factorial variable
    factorial = 1
    # We start multiplication from 1

    # Initialize counter
    i = 1

    # Using while loop
    while i <= n:
        # Multiply factorial by current value of i
        factorial *= i
        # Same as: factorial = factorial * i

        # Increase counter
        i += 1

    # Print the result
    print("Factorial of", n, "is", factorial)