# Q10. Write a program to check whether a given string
# is a palindrome after removing spaces, punctuation marks,
# and converting all characters to lowercase.

import string

text = input("Enter a string : ")

# converting into lowercase
text = text.lower()

new_text = ""

# removing spaces and punctuation
for ch in text:

    if ch not in string.punctuation and ch != " ":
        new_text = new_text + ch

# checking palindrome
reverse = new_text[::-1]

if new_text == reverse:

    print("The string is a Palindrome")

else:

    print("The string is Not a Palindrome")