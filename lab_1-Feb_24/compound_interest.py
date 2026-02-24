# Problem 5
# Calculate Compound Interest

# Taking principal amount from user
principal = float(input("Enter Principal Amount: "))
# Converted to float because money may include decimal values

# Taking rate of interest from user
rate = float(input("Enter Rate of Interest (per year): "))
# Converted to float for decimal flexibility

# Taking time from user
time = float(input("Enter Time (in years): "))
# Converted to float because time may not always be whole number

# Calculating total amount using compound interest formula
amount = principal * (1 + rate / 100) ** time
# (rate / 100) converts percentage into decimal
# (1 + rate/100) calculates growth factor
# ** time means power (compound for 'time' years)

# Calculating compound interest
compound_interest = amount - principal
# CI = Total Amount - Principal

# Printing results
print("\nTotal Amount =", amount)
print("Compound Interest =", compound_interest)