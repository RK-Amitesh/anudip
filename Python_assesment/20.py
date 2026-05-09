# Q20. Create a file processing program that
# handles file not found errors and counts
# total words, lines, and characters in a text file.

try:

    file = open("sample.txt", "r")

    data = file.read()

    # counting characters
    characters = len(data)

    # counting words
    words = len(data.split())

    # counting lines
    file.seek(0)

    lines = len(file.readlines())

    print("Total Lines =", lines)
    print("Total Words =", words)
    print("Total Characters =", characters)

    file.close()

# handling file not found error
except FileNotFoundError:

    print("File Not Found")

# handling other errors
except Exception as e:

    print("Error :", e)