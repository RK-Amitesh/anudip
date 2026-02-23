# ==================================================
# This program calculates the Compound Interest
# Formula:
# A = P(1 + R/100)^T
# Compound Interest = A - P
# ==================================================

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (%): "))
time = float(input("Enter time in years: "))

# Calculating final amount
amount = principal * (1 + rate/100) ** time

# Calculating compound interest
compound_interest = amount - principal

print("Compound Interest:", compound_interest)