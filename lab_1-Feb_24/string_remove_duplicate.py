# Problem 95
# Remove duplicate characters from string

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)