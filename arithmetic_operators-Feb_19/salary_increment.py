# ==================================================
# this program calculates the Increment in Salary
# based on the given percentage

# Increment Amount = (Salary × Increment %) / 100
# New Salary = Salary + Increment Amount
# ==================================================

salary = float(input("Enter current salary: "))
increment_percent = float(input("Enter increment percentage: "))

increment_amount = (salary * increment_percent) / 100
new_salary = salary + increment_amount

print("Increment Amount:", increment_amount)
print("New Salary:", new_salary)