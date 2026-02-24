# Problem 13
# Check whether a character is vowel or consonant

# Taking input from user
ch = input("Enter a single alphabet: ")
# input() takes string
# Stored in variable 'ch'

# Check if input length is 1
if len(ch) != 1:
    # If user enters more than one character
    print("Please enter only one character.")

# Check if it is an alphabet
elif not ch.isalpha():
    # isalpha() returns True if character is alphabet
    print("Entered character is not an alphabet.")

# Convert character to lowercase for easy comparison
elif ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    # lower() converts uppercase to lowercase
    # Check if character is in vowel list
    print("It is a Vowel.")

else:
    # If not vowel but alphabet, it must be consonant
    print("It is a Consonant.")