# Q15. Write a Pandas program to read employee data
# from a CSV file and display department-wise
# average salary and highest salary employee.

import pandas as pd

# reading csv file
data = pd.read_csv("employee.csv")

print("Employee Data :\n")
print(data)

# department-wise average salary
print("\nDepartment-wise Average Salary :")

avg_salary = data.groupby("Department")["Salary"].mean()

print(avg_salary)

# finding highest salary employee
highest = data.loc[data["Salary"].idxmax()]

print("\nHighest Salary Employee :")
print(highest)