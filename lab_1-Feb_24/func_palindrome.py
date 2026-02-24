# Problem 43
# Check palindrome string using function

# Define function to check palindrome
def is_palindrome(text):

    # Convert string to lowercase
    text = text.lower()

    # Initialize empty string for reversed text
    reversed_text = ""

    # Reverse string using loop
    for ch in text:
        reversed_text = ch + reversed_text

    # Compare original and reversed string
    if text == reversed_text:
        return True
    else:
        return False


# Taking input from user
user_input = input("Enter a string: ")

# Call the function
result = is_palindrome(user_input)

# Display result
if result:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")