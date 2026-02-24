# Problem 96
# Find first non-repeating character

text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found.")