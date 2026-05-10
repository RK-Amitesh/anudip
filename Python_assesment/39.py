# Q39. Read a CSV file containing student
# attendance records and display students
# with attendance below 75%.

import pandas as pd

# reading csv file
data = pd.read_csv("student_attendance.csv")

print("Student Attendance Data :\n")
print(data)

print("\nStudents with Attendance Below 75% :\n")

# checking attendance
low_attendance = data[data["Attendance"] < 75]

print(low_attendance)