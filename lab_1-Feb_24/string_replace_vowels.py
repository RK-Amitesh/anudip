# Problem 93
# Replace all vowels with *

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print("Modified string:", result)