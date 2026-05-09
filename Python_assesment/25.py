# Q25. Store word frequencies from a text file
# into a dictionary and display the top five
# most frequently used words.

file = open("data.txt", "r")

data = file.read().lower()

words = data.split()

freq = {}

# counting word frequency
for i in words:

    if i in freq:

        freq[i] = freq[i] + 1

    else:

        freq[i] = 1

# sorting dictionary
sorted_words = sorted(freq.items(),
                    key=lambda x: x[1],
                    reverse=True)

print("Top Five Most Frequent Words :\n")

for i in sorted_words[:5]:

    print(i[0], "=", i[1])

file.close()