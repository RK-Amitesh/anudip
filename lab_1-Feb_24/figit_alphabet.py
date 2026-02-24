# Problem 14
# Check whether a character is digit or alphabet

# Taking input from user
ch = input("Enter a single character: ")
# input() takes string
# Stored in variable 'ch'

# Check if user entered exactly one character
if len(ch) != 1:
    # If length is not equal to 1
    print("Please enter only one character.")

# Check if character is alphabet
elif ch.isalpha():
    # isalpha() returns True if character is A-Z or a-z
    print("It is an Alphabet.")

# Check if character is digit
elif ch.isdigit():
    # isdigit() returns True if character is 0-9
    print("It is a Digit.")

else:
    # If it is neither alphabet nor digit
    print("It is a Special Character.")