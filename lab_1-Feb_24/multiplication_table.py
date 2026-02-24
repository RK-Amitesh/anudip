# Problem 28
# Print multiplication table using while loop

# Taking input from user
num = int(input("Enter a number to print its multiplication table: "))
# Convert input string to integer

# Initialize counter
i = 1
# We will multiply from 1 to 10

print("Multiplication Table of", num)

# Using while loop
while i <= 10:
    # Calculate product
    result = num * i

    # Print in formatted way
    print(num, "x", i, "=", result)

    # Increase counter
    i += 1