# Problem 38
# Reverse a string using for loop

# Taking input from user
text = input("Enter a string: ")
# input() stores entire line as string

# Initialize empty string to store reversed result
reversed_text = ""

# Loop from last index to first index
for i in range(len(text) - 1, -1, -1):
    # len(text) - 1 → last index
    # -1 → stop before index -1
    # -1 → step backward

    reversed_text += text[i]
    # Add character at index i to reversed string

# Print result
print("Reversed string:", reversed_text)