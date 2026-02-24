# Problem 46
# Generate Fibonacci series using function

# Define Fibonacci function
def fibonacci(n):

    # Check for valid input
    if n <= 0:
        print("Please enter a positive number.")
        return

    # First two Fibonacci numbers
    first = 0
    second = 1

    print("Fibonacci Series:")

    # Loop for n terms
    for i in range(n):
        print(first)

        # Generate next term
        next_term = first + second

        # Update values
        first = second
        second = next_term


# Taking input from user
num = int(input("Enter number of terms: "))

# Call function
fibonacci(num)