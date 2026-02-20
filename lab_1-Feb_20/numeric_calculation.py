"""Description:
    A simple calculator module that performs addition and subtraction of two numbers using reusable functions.

    This script demonstrates:
    - Function usage
    - Input validation
    - Clean and maintainable coding practices"""

def add_numbers(num1: float, num2: float) -> float:
    """Returns the sum of two numbers."""
    return num1 + num2


def subtract_numbers(num1: float, num2: float) -> float:
    """Returns the difference between two numbers."""
    return num1 - num2


def get_user_input() -> tuple:
    """Takes numeric input from the user and validates it.
        Returns-> tuple: Two float numbers entered by the user"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        exit()


def main():
    """Main function to execute calculator operations."""
    print("\n===== Simple Calculator =====\n")

    num1, num2 = get_user_input()

    addition_result = add_numbers(num1, num2)
    subtraction_result = subtract_numbers(num1, num2)

    print("\n----- Results -----")
    print(f"Addition: {num1} + {num2} = {addition_result}")
    print(f"Subtraction: {num1} - {num2} = {subtraction_result}")
    print("\n==============================\n")


if __name__ == "__main__":
    main()