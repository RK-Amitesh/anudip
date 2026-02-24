# Problem 34
# Find sum of first N natural numbers using for loop

# Taking input from user
n = int(input("Enter a number N: "))
# Convert input string into integer

# Check if input is valid
if n <= 0:
    print("Please enter a positive number.")

else:
    # Initialize sum variable
    total_sum = 0

    # Loop from 1 to N
    for i in range(1, n + 1):
        total_sum += i
        # Same as: total_sum = total_sum + i

    # Print result
    print("Sum of first", n, "natural numbers is:", total_sum)