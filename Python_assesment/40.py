# Q40. Design a mini student management system
# using functions, dictionaries, file handling,
# exception handling, and Pandas for report generation.

import pandas as pd
import os

# fixed file path
filename = r"C:\Users\AMITESH\OneDrive\Desktop\python\Python_assesment\students.csv"

# checking if file exists
if not os.path.exists(filename):

    file = open(filename, "w")

    file.write("Name,Marks,Course\n")

    file.close()

    print("students.csv file created successfully")

else:

    print("students.csv file already exists")


# function to add student
def add_student():

    try:

        name = input("Enter student name : ")
        marks = int(input("Enter marks : "))
        course = input("Enter course : ")

        # append mode
        file = open(filename, "a")

        file.write(f"{name},{marks},{course}\n")

        file.close()

        print("Student Record Added")

    except Exception as e:

        print("Error :", e)


# function to display report
def display_report():

    try:

        data = pd.read_csv(filename)

        print("\nStudent Report :\n")

        print(data)

        print("\nAverage Marks =",
              data["Marks"].mean())

    except Exception as e:

        print("Error :", e)


# menu-driven program
while True:

    print("\n----- Student Management Menu -----")
    print("1. Add Student")
    print("2. Display Report")
    print("3. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        add_student()

    elif choice == 2:

        display_report()

    elif choice == 3:

        print("Exiting Program")
        break

    else:

        print("Invalid Choice")
        