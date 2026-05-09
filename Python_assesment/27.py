# Q27. Create tuples containing student names
# and courses. Convert them into sets to identify
# students enrolled in multiple courses.

course1 = (
    "Amit",
    "Rahul",
    "Mohit",
    "Riya"
)

course2 = (
    "Rahul",
    "Riya",
    "Karan",
    "Simran"
)

# converting tuples into sets
set1 = set(course1)
set2 = set(course2)

# finding common students
multiple_courses = set1.intersection(set2)

print("Students in Course 1 :")
print(set1)

print("\nStudents in Course 2 :")
print(set2)

print("\nStudents Enrolled in Multiple Courses :")
print(multiple_courses)