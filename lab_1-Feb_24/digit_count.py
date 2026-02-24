# Problem 24
# Count digits in a number

# Taking input from user
num = int(input("Enter a number: "))
# Convert input string into integer
# Store in variable 'num'

# If number is negative, convert to positive
num = abs(num)
# abs() ensures digit counting works properly

# Special case: if number is 0
if num == 0:
    count = 1
else:
    # Initialize digit counter
    count = 0

    # Using while loop to remove digits one by one
    while num > 0:
        num = num // 10
        # Integer division removes last digit

        count += 1
        # Increase digit counter by 1

# Print result
print("Total number of digits:", count)