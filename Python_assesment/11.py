# Q11. Create a text file containing student marks.
# Read the file and display the topper,
# average marks, and students scoring below average.

file = open("marks.txt", "r")

data = file.readlines()

students = []
total = 0

for line in data:

    parts = line.split()

    name = parts[0]
    marks = int(parts[1])

    students.append((name, marks))

    total = total + marks

average = total / len(students)

# topper
topper = students[0]

for i in students:

    if i[1] > topper[1]:

        topper = i

print("Topper :", topper[0], "-", topper[1])

print("Average Marks =", average)

print("\nStudents Below Average :")

for i in students:

    if i[1] < average:

        print(i[0], "-", i[1])

file.close()