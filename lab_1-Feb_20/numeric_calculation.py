"""
File: numeric_calculation.py
Description:
    Performs basic arithmetic operations:
    Addition, Subtraction, Multiplication, and Division.
"""


# Function to return sum of two numbers
def add(a: float, b: float) -> float:
    return a + b


# Function to return difference of two numbers
def subtract(a: float, b: float) -> float:
    return a - b


# Function to return product of two numbers
def multiply(a: float, b: float) -> float:
    return a * b


# Function to return division of two numbers
def divide(a: float, b: float) -> float:
    if b == 0:  # Prevent division by zero
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def main():
    """Main function to execute program."""

    try:
        # Taking user input and converting to float
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\n---- Results ----")

        # Calling arithmetic functions
        print(f"Addition: {add(num1, num2)}")
        print(f"Subtraction: {subtract(num1, num2)}")
        print(f"Multiplication: {multiply(num1, num2)}")

        # Handling division separately to catch zero division error
        try:
            print(f"Division: {divide(num1, num2)}")
        except ZeroDivisionError as error:
            print(f"Division Error: {error}")

    except ValueError:
        # Handles invalid numeric input
        print("Invalid input! Please enter numeric values only.")


# Ensures main() runs only when file is executed directly
if __name__ == "__main__":
    main()