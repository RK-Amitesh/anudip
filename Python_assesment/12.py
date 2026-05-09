# Q12. Develop a calculator program that handles
# division by zero, invalid inputs, and incorrect
# operations using multiple exception blocks.

try:

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("\nChoose Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        print("Result =", num1 + num2)

    elif choice == 2:

        print("Result =", num1 - num2)

    elif choice == 3:

        print("Result =", num1 * num2)

    elif choice == 4:

        print("Result =", num1 / num2)

    else:

        print("Invalid Operation")

# handling division by zero
except ZeroDivisionError:

    print("Division by Zero is Not Allowed")

# handling invalid input
except ValueError:

    print("Please Enter Valid Numeric Value")

# handling any other error
except Exception as e:

    print("Error :", e)