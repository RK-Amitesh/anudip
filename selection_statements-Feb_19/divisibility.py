# Divisible by 5 and 11
# Program to check whether a number is divisible by both 5 and 11

# Input number
num = int(input("Enter a number: "))

# Checking condition
if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by both 5 and 11")
else:
    print("Number is NOT divisible by both 5 and 11")