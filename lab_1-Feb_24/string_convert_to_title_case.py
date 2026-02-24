# Problem 91
# Convert string to title case manually

text = input("Enter a sentence: ")

words = text.split()   # Split sentence into words
result = ""

for word in words:
    # Capitalize first letter and keep rest lowercase
    result += word[0].upper() + word[1:].lower() + " "

print("Title Case:", result.strip())
# strip() removes extra space at end