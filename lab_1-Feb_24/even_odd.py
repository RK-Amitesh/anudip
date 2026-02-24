# Problem 8
# Check whether a number is even or odd WITHOUT using modulus operator

# Taking input from user
num = int(input("Enter a number: "))
# Converts input string into integer
# Stores value in variable 'num'

# Checking even or odd without using %

if (num // 2) * 2 == num:
    # num // 2 performs integer division
    # Multiply result by 2
    # If it equals original number, it means no remainder
    # Therefore, number is EVEN
    print("The number is Even.")

else:
    # If above condition is False,
    # It means remainder exists when divided by 2
    # Therefore, number is ODD
    print("The number is Odd.")