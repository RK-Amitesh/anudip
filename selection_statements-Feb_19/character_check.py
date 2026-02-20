# Character Type Check
# Program to check whether input is alphabet, digit or special character

# Input character
ch = input("Enter a character: ")

# Checking condition
if ch.isalpha():
    print("It is an Alphabet")
elif ch.isdigit():
    print("It is a Digit")
else:
    print("It is a Special Character")