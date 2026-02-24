# Problem 47
# Count vowels using function

# Define function
def count_vowels(text):

    # Initialize vowel counter
    count = 0

    # Loop through each character
    for ch in text:
        # Check if character is vowel
        if ch.lower() in "aeiou":
            # Convert to lowercase for easy comparison
            count += 1

    return count


# Taking input from user
user_input = input("Enter a string: ")

# Call function
result = count_vowels(user_input)

# Print result
print("Number of vowels:", result)