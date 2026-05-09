# Q18. Develop a frequency counter that stores
# occurrence of each word from a paragraph
# into a dictionary and displays the most repeated word.

para = input("Enter a paragraph : ")

# converting into lowercase
para = para.lower()

words = para.split()

data = {}

# counting frequency of words
for i in words:

    if i in data:

        data[i] = data[i] + 1

    else:

        data[i] = 1

print("\nWord Frequencies :")

for i in data:

    print(i, "=", data[i])

# finding most repeated word
max_word = ""
max_count = 0

for i in data:

    if data[i] > max_count:

        max_count = data[i]
        max_word = i

print("\nMost Repeated Word :", max_word)
print("Frequency :", max_count)
