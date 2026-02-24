# Problem 45
# Find sum of digits using function

# Define function
def sum_of_digits(num):

    # Convert negative number to positive
    num = abs(num)

    # Initialize sum variable
    total = 0

    # Loop until number becomes 0
    while num > 0:
        digit = num % 10
        # Extract last digit

        total += digit
        # Add digit to total

        num = num // 10
        # Remove last digit

    return total


# Taking input from user
number = int(input("Enter a number: "))

# Call function
result = sum_of_digits(number)

# Print result
print("Sum of digits is:", result)