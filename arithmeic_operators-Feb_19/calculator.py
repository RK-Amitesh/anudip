# ====================================================================
# This program performs basic arithmetic operations:
# Addition (+), Subtraction (-), Multiplication (*), and Division (/).
# The operation is selected by the user.
# ====================================================================

# Taking first number from user
num1 = float(input("Enter first number: "))

# Taking second number from user
num2 = float(input("Enter second number: "))

# Taking operator input
operator = input("Enter operator (+, -, *, /): ")

# Checking which operator the user selected
if operator == "+":
    # Addition operation
    result = num1 + num2
    print("Addition Result:", result)

elif operator == "-":
    # Subtraction operation
    result = num1 - num2
    print("Subtraction Result:", result)

elif operator == "*":
    # Multiplication operation
    result = num1 * num2
    print("Multiplication Result:", result)

elif operator == "/":
    # Division operation
    # Division by zero is not allowed
    if num2 != 0:
        result = num1 / num2
        print("Division Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator entered.")