# Problem 39
# Calculate power without using exponent operator

# Taking input from user
base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

# Initialize result to 1
result = 1

# Handle negative exponent
if exponent < 0:
    # Convert exponent to positive
    exponent = abs(exponent)

    # Multiply base exponent times
    for i in range(exponent):
        result *= base

    # Take reciprocal for negative exponent
    result = 1 / result

else:
    # Multiply base exponent times
    for i in range(exponent):
        result *= base

# Print result
print("Result:", result)