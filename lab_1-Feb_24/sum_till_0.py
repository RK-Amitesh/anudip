# Problem 30
# Accept numbers until 0 is entered and print sum

# Initialize sum variable
total_sum = 0
# This will store the running total

print("Enter numbers (Enter 0 to stop):")

# Infinite loop
while True:
    # Take input from user
    num = int(input("Enter number: "))
    # Convert input string to integer

    # Check if user entered 0
    if num == 0:
        # Stop the loop
        break

    # Add number to total
    total_sum += num
    # Same as: total_sum = total_sum + num

# After loop ends
print("Total sum is:", total_sum)