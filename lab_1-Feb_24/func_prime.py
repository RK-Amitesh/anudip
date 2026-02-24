# Problem 41
# Check prime number using function

# Define function to check prime
def is_prime(num):
    # If number is less than or equal to 1, not prime
    if num <= 1:
        return False

    # Check divisibility from 2 to square root of number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            # If divisible, not prime
            return False

    # If no divisor found, number is prime
    return True


# Taking input from user
number = int(input("Enter a number: "))

# Call the function and store result
result = is_prime(number)

# Display result
if result:
    print(number, "is a Prime number.")
else:
    print(number, "is NOT a Prime number.")