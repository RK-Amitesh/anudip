# Problem 23
# Reverse a number using while loop

# Taking input from user
num = int(input("Enter a number: "))
# Convert input string to integer
# Store in variable 'num'

# Store original number for display
original = num

# If number is negative, handle separately
is_negative = False

if num < 0:
    is_negative = True
    num = abs(num)
    # Convert to positive for processing

# Initialize reverse variable
reverse = 0

# Using while loop
while num > 0:
    # Extract last digit
    digit = num % 10
    # % 10 gives last digit

    # Add digit to reversed number
    reverse = reverse * 10 + digit
    # Shift digits left and add new digit

    # Remove last digit from original number
    num = num // 10

# Restore negative sign if needed
if is_negative:
    reverse = -reverse

# Print result
print("Reversed number is:", reverse)