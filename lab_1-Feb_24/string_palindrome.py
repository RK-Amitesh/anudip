# Problem 87
# Check whether string is palindrome

text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
text = text.lower()

if text == text[::-1]:
    print("String is a Palindrome.")
else:
    print("String is NOT a Palindrome.")