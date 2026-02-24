# Problem 48
# Find GCD using function (Euclidean Algorithm)

# Define GCD function
def find_gcd(a, b):

    # Convert numbers to positive
    a = abs(a)
    b = abs(b)

    # Apply Euclidean Algorithm
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    # When b becomes 0, a contains GCD
    return a


# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Call function
result = find_gcd(num1, num2)

# Print result
print("GCD is:", result)