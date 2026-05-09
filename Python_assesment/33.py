# Q33. Create a program that copies contents
# from one file to another and displays
# the total number of words copied.

source = open("source.txt", "r")

data = source.read()

destination = open("destination.txt", "w")

# copying data
destination.write(data)

# counting words
words = len(data.split())

print("File Copied Successfully")
print("Total Words Copied =", words)

source.close()
destination.close()