# Problem 10
# Reverse a given number

# Taking input from user
num = int(input("Enter a number: "))
# Convert input string to integer
# Store in variable 'num'

# Store original number (optional, for display purpose)
original_num = num

# If number is negative, handle separately
is_negative = False
# Flag variable to check if number is negative

if num < 0:
    is_negative = True
    # Mark number as negative
    num = abs(num)
    # Convert to positive for reversing process

# Initialize reverse variable
reverse = 0
# This will store the reversed number

# Loop until number becomes 0
while num > 0:
    # Extract last digit
    digit = num % 10
    # % 10 gives last digit

    # Append digit to reverse
    reverse = reverse * 10 + digit
    # Shift existing digits left (×10)
    # Add extracted digit at unit place

    # Remove last digit from num
    num = num // 10
    # Integer division removes last digit

# If original number was negative, restore sign
if is_negative:
    reverse = -reverse

# Print result
print("Reversed number =", reverse)