# Q26. Write a program to separate vowels
# and consonants from a sentence and
# store them in different lists.

text = input("Enter a sentence : ")

vowels = []
consonants = []

# converting into lowercase
text = text.lower()

for ch in text:

    # checking alphabet
    if ch.isalpha():

        if ch in "aeiou":

            vowels.append(ch)

        else:

            consonants.append(ch)

print("\nVowels List :")
print(vowels)

print("\nConsonants List :")
print(consonants)