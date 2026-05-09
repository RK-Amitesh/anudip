# Q1. Write a Python program that accepts a paragraph from the user
# and calculates the number of uppercase letters, lowercase letters,
# digits, spaces, and special characters.
# Display the result in descending order based on frequency.

para = input("Enter a paragraph : ")

upper = 0
lower = 0
digit = 0
space = 0
special = 0

# checking each character
for ch in para:

    if ch.isupper():
        upper = upper + 1

    elif ch.islower():
        lower = lower + 1

    elif ch.isdigit():
        digit = digit + 1

    elif ch.isspace():
        space = space + 1

    else:
        special = special + 1

# storing values in dictionary
data = {
    "Uppercase": upper,
    "Lowercase": lower,
    "Digits": digit,
    "Spaces": space,
    "Special Characters": special
}

# sorting in descending order
sorted_data = sorted(data.items(),key=lambda x: x[1],reverse=True)

print("\nResult in Descending Order")

for i in sorted_data:
    print(i[0], "=", i[1])