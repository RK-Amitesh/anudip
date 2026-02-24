# Problem 42
# Find factorial using function

# Define factorial function
def factorial(n):
    # Check if number is negative
    if n < 0:
        return None  # Factorial not defined for negative numbers

    # Initialize result
    result = 1

    # Loop from 1 to n
    for i in range(1, n + 1):
        result *= i
        # Same as result = result * i

    return result


# Taking input from user
num = int(input("Enter a number: "))

# Call the function
fact = factorial(num)

# Check result
if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", fact)