# =============================================================
# This program calculates the Body Mass Index (BMI) of a person
# Formula:
#
#     BMI = Weight (kg) / (Height (m))²
#
# It uses arithmetic operators:
# Division (/) and Exponentiation (**)
#
# BMI Categories:
# < 18.5      → Underweight
# 18.5 - 24.9 → Normal weight
# 25 - 29.9   → Overweight
# ≥ 30        → Obese
# =============================================================

# Taking weight in kilograms
weight = float(input("Enter your weight in kilograms: "))

# Taking height in meters
height = float(input("Enter your height in meters: "))

# Calculating BMI using formula
# height ** 2 means height squared
bmi = weight / (height ** 2)

# Displaying BMI value
print("Your BMI is:", bmi)

# Checking BMI category
if bmi < 18.5:
    print("Category: Underweight")

elif bmi < 25:
    print("Category: Normal weight")

elif bmi < 30:
    print("Category: Overweight")

else:
    print("Category: Obese")