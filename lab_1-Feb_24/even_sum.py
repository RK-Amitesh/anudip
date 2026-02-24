# Problem 25
# Find sum of even numbers up to N

# Taking input from user
n = int(input("Enter a number N: "))
# Convert input string to integer
# Store value in variable 'n'

# Initialize counter
i = 1

# Initialize sum variable
sum_even = 0
# This will store the total sum of even numbers

# Using while loop
while i <= n:
    # Check if current number is even
    if i % 2 == 0:
        # If remainder when divided by 2 is 0
        sum_even += i
        # Add even number to sum

    # Increase counter
    i += 1

# Print the result
print("Sum of even numbers up to", n, "is:", sum_even)