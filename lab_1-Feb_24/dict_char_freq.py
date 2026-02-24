# Problem 77
# Count character frequency using dictionary

text = input("Enter a string: ")

frequency = {}  # Empty dictionary

# Loop through each character
for ch in text:
    
    # If character already exists in dictionary
    if ch in frequency:
        frequency[ch] += 1  # Increase count
    else:
        frequency[ch] = 1   # Add new character

# Print frequency
for key, value in frequency.items():
    print(key, ":", value)