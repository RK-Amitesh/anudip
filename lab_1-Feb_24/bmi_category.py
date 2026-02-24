# Problem 18
# Calculate BMI and determine category

# Taking weight input from user
weight = float(input("Enter weight in kilograms: "))
# Converted to float to allow decimal values

# Taking height input from user
height = float(input("Enter height in meters: "))
# Converted to float because height may contain decimals

# Checking if height is valid (cannot be zero)
if height <= 0:
    print("Invalid height entered.")

else:
    # Calculating BMI using formula
    bmi = weight / (height ** 2)
    # height ** 2 means height squared
    # Division gives BMI value

    print("\nYour BMI is:", bmi)

    # Categorizing BMI using if-elif ladder
    if bmi < 18.5:
        print("Category: Underweight")

    elif bmi < 25:
        # 18.5 <= BMI < 25
        print("Category: Normal weight")

    elif bmi < 30:
        # 25 <= BMI < 30
        print("Category: Overweight")

    else:
        # BMI >= 30
        print("Category: Obese")