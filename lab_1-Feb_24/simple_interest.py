# Problem 4
# Calculate Simple Interest

# Taking principal amount from user
principal = float(input("Enter Principal Amount: "))
# input() takes value as string
# float() converts it into decimal number (for money calculations)
# Value stored in variable 'principal'

# Taking rate of interest from user
rate = float(input("Enter Rate of Interest (per year): "))
# Converted to float because rate may contain decimal value

# Taking time from user
time = float(input("Enter Time (in years): "))
# Converted to float for flexibility (can be 2.5 years etc.)

# Calculating Simple Interest using formula
simple_interest = (principal * rate * time) / 100
# Multiply principal, rate and time
# Divide the result by 100 as per formula

# Printing the result
print("\nSimple Interest =", simple_interest)