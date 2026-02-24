# Problem 86
# Reverse a string without slicing

text = input("Enter a string: ")

reversed_text = ""

# Loop through string
for ch in text:
    # Add character at beginning
    reversed_text = ch + reversed_text

print("Reversed string:", reversed_text)