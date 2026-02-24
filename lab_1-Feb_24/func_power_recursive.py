# Problem 50
# Calculate power using recursive function

# Define recursive function
def power(base, exponent):

    # Base case
    if exponent == 0:
        return 1
        # Any number raised to power 0 is 1

    # Handle negative exponent
    if exponent < 0:
        return 1 / power(base, -exponent)

    # Recursive case
    return base * power(base, exponent - 1)
    # Multiply base with power(base, exponent-1)


# Taking input from user
base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

# Call function
result = power(base, exponent)

# Print result
print("Result:", result)