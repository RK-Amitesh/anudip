# Problem 31
# Print all prime numbers between 1 and N

# Taking input from user
n = int(input("Enter a number N: "))
# Convert input string to integer

print("Prime numbers between 1 and", n, "are:")

# Loop from 2 to N
num = 2
while num <= n:

    # Assume number is prime
    is_prime = True

    # Check divisibility from 2 to num-1
    divisor = 2
    while divisor * divisor <= num:
        # Check only up to square root of number

        if num % divisor == 0:
            # If divisible, not prime
            is_prime = False
            break

        divisor += 1

    # If number is prime, print it
    if is_prime:
        print(num)

    # Move to next number
    num += 1