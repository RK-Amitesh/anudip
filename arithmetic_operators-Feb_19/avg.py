# ==========================================================
# This program calculates the average of Five Numbers
# ----------------------------------------------------------
# Formula:
# Average = (Sum of all numbers) / Total count
# ==========================================================

# Taking inputs
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))
n5 = float(input("Enter fifth number: "))

# Calculating total
total = n1 + n2 + n3 + n4 + n5

# Calculating average
average = total / 5

print("Average:", average)