# ==================================================
# This program calculates the Simple Interest
# Formula:
# Simple Interest (SI) = (P × R × T) / 100
# P = Principal
# R = Rate of interest
# T = Time (years)
# ==================================================

# Taking inputs
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = float(input("Enter time in years: "))

# Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Display result
print("Simple Interest:", simple_interest)