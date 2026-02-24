# Problem 35
# Count vowels in a string

# Taking input from user
text = input("Enter a string: ")
# input() stores entire line as string

# Convert string to lowercase
text = text.lower()
# This makes checking easier (A and a treated same)

# Initialize vowel counter
vowel_count = 0

# Loop through each character in string
for ch in text:
    # Check if character is vowel
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
        # Increase count if vowel found

# Print result
print("Number of vowels:", vowel_count)