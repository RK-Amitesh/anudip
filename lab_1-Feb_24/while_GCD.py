# Problem 29
# Find GCD using while loop (Euclidean Algorithm)

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Convert numbers to positive (GCD is always positive)
a = abs(a)
b = abs(b)

# Using while loop
while b != 0:
    # Store remainder of a divided by b
    remainder = a % b

    # Update a to b
    a = b

    # Update b to remainder
    b = remainder

# When b becomes 0, a contains GCD
print("GCD is:", a)