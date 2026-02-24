# Problem 9
# Find the sum of digits of a number

# Taking input from user
num = int(input("Enter a number: "))
# Convert input string into integer
# Store in variable 'num'

# If number is negative, convert to positive
num = abs(num)
# abs() makes number positive
# This ensures digit extraction works correctly

# Initialize sum variable
sum_of_digits = 0
# This variable will store the final sum

# Loop until number becomes 0
while num > 0:
    # Extract last digit
    digit = num % 10
    # % 10 gives remainder when divided by 10
    # This remainder is the last digit

    # Add digit to sum
    sum_of_digits += digit
    # Same as: sum_of_digits = sum_of_digits + digit

    # Remove last digit
    num = num // 10
    # Integer division removes the last digit

# Print the result
print("Sum of digits =", sum_of_digits)