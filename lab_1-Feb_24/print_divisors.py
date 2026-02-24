# Problem 36
# Print all divisors of a number

# Taking input from user
num = int(input("Enter a number: "))
# Convert input string to integer

# Convert negative number to positive
num = abs(num)

# Check if number is zero
if num == 0:
    print("Every number divides 0. Divisors are undefined.")
else:
    print("Divisors of", num, "are:")

    # Loop from 1 to num
    for i in range(1, num + 1):
        # Check if i divides num completely
        if num % i == 0:
            print(i)