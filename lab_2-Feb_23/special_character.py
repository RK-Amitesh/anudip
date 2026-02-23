# -------------------------------------------------------------
# Program Name : Count Special Characters
# Description  :
# This program counts the number of special characters
# in a given sentence.
# Special characters are those which are:
# 1. Not alphabets (A-Z, a-z)
# 2. Not digits (0-9)
# 3. Not space
# Examples: ! @ # $ % ^ & * ( ) _ + etc.
# -------------------------------------------------------------

# Step 1: Take input from user
sentence = input("Enter a sentence: ")

# Step 2: Initialize counter variable
special_count = 0

# Step 3: Traverse each character in the sentence
for ch in sentence:
    
    # Check if character is NOT alphabet AND NOT digit AND NOT space
    if not ch.isalnum() and ch != " ":
        special_count += 1   # Increase counter

# Step 4: Display result
print("Number of special characters:", special_count)