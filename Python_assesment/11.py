# Q11. Create a text file containing student marks.
# Read the file and display the topper,
# average marks, and students scoring below average.

file = open("marks.txt", "r")

data = file.readlines()

students = []
total = 0

for line in data:

    temp = line.split()

    name = temp[0]
    marks = int(temp[1])

    students.append((name, marks))

    total = total + marks

# calculating average
average = total / len(students)

# finding topper
topper = students[0]

for i in students:

    if i[1] > topper[1]:

        topper = i

print("Topper :", topper[0], "-", topper[1])

print("Average Marks =", average)

print("\nStudents Scoring Below Average :")

for i in students:

    if i[1] < average:

        print(i[0], "-", i[1])

file.close()