# Q7. Create a program that stores employee records in tuples.
# Each tuple should contain employee ID, name, and salary.
# Display employees whose salary is above the average salary.

employees = []

n = int(input("Enter number of employees : "))

# taking employee details
for i in range(n):

    emp_id = int(input("\nEnter Employee ID : "))
    name = input("Enter Employee Name : ")
    salary = int(input("Enter Employee Salary : "))

    data = (emp_id, name, salary)

    employees.append(data)

# calculating average salary
total = 0

for i in employees:
    total = total + i[2]

average = total / n

print("\nAverage Salary =", average)

print("\nEmployees having salary above average :")

for i in employees:

    if i[2] > average:

        print("ID =", i[0],
            "Name =", i[1],
            "Salary =", i[2])