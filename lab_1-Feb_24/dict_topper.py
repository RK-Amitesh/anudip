# Problem 76
# Create student marks dictionary and find topper

# Ask number of students
n = int(input("Enter number of students: "))

students = {}  # Create empty dictionary

# Loop to take input for each student
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    
    # Store name as key and marks as value
    students[name] = marks

# Find topper (key with maximum value)
topper = max(students, key=students.get)

print("Topper is:", topper)
print("Marks:", students[topper])