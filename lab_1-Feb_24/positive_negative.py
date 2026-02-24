# Problem 2
# Check whether a number is positive, negative, or zero

# Taking input from the user
num = int(input("Enter a number: "))
# input() takes value as string
# int() converts that string into integer
# The integer value is stored in variable 'num'

# Checking the condition using if-elif-else

if num > 0:
    # This block runs only if number is greater than 0
    print("The number is Positive.")

elif num < 0:
    # This block runs only if number is less than 0
    print("The number is Negative.")

else:
    # This block runs if none of the above conditions are True
    # That means the number is exactly 0
    print("The number is Zero.")