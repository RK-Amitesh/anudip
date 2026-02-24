# Problem 37
# Generate Fibonacci series using for loop

# Taking number of terms from user
n = int(input("Enter number of terms: "))
# Convert input string to integer

# Check for valid input
if n <= 0:
    print("Please enter a positive number.")

else:
    # First two Fibonacci numbers
    first = 0
    second = 1

    print("Fibonacci Series:")

    # Using for loop
    for i in range(n):
        # Print current first number
        print(first)

        # Generate next term
        next_term = first + second

        # Update values for next iteration
        first = second
        second = next_term