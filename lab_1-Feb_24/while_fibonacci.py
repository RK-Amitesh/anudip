# Problem 27
# Generate Fibonacci series using while loop

# Taking number of terms from user
n = int(input("Enter number of terms: "))
# Convert input string to integer

# Check if number is valid
if n <= 0:
    print("Please enter a positive number.")

else:
    # First two Fibonacci numbers
    first = 0
    second = 1

    # Counter to track number of printed terms
    count = 0

    print("Fibonacci Series:")

    # Using while loop
    while count < n:
        print(first)

        # Generate next term
        next_term = first + second

        # Update values for next iteration
        first = second
        second = next_term

        # Increase counter
        count += 1