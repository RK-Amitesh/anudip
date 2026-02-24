# Problem 19
# Check whether a number lies within a given range

# Taking number input
num = float(input("Enter the number to check: "))
# Converted to float to allow decimal numbers

# Taking lower limit of range
lower = float(input("Enter lower limit of range: "))

# Taking upper limit of range
upper = float(input("Enter upper limit of range: "))

# Check if range is valid
if lower > upper:
    # If lower limit is greater than upper limit
    print("Invalid range entered.")

# Checking if number lies within the range
elif lower <= num <= upper:
    # This is chained comparison
    # It checks: lower <= num AND num <= upper
    print("The number lies within the range.")

else:
    # If above condition is False
    print("The number does NOT lie within the range.")