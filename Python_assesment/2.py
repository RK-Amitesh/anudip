# Q2. Develop a grading system where marks of five subjects
# are entered by the user. The program should calculate
# percentage, assign grades using nested if-else conditions,
# and identify whether the student qualifies for scholarship.

m1 = int(input("Enter marks of Subject 1 : "))
m2 = int(input("Enter marks of Subject 2 : "))
m3 = int(input("Enter marks of Subject 3 : "))
m4 = int(input("Enter marks of Subject 4 : "))
m5 = int(input("Enter marks of Subject 5 : "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\nTotal Marks =", total)
print("Percentage =", percentage)

# grading system
if percentage >= 90:
    grade = "A+"

    if percentage >= 95:
        scholarship = "Eligible for Scholarship"
    else:
        scholarship = "Not Eligible for Scholarship"

elif percentage >= 75:
    grade = "A"
    scholarship = "Not Eligible for Scholarship"

elif percentage >= 60:
    grade = "B"
    scholarship = "Not Eligible for Scholarship"

elif percentage >= 40:
    grade = "C"
    scholarship = "Not Eligible for Scholarship"

else:
    grade = "Fail"
    scholarship = "Not Eligible for Scholarship"

print("Grade =", grade)
print(scholarship)