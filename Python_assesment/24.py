# Q24. Create a function for division of two numbers
# and use exception handling to validate inputs
# and avoid runtime errors.

def divide(a, b):

    result = a / b

    return result


try:

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    answer = divide(num1, num2)

    print("Division Result =", answer)

# handling division by zero
except ZeroDivisionError:

    print("Division by Zero is Not Allowed")

# handling invalid input
except ValueError:

    print("Please Enter Valid Numbers")

# handling other errors
except Exception as e:

    print("Error :", e)