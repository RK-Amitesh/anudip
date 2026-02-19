# Program to calculate income tax based on Indian tax slabs

# taking input
income = float(input("Enter your annual income: "))
age = int(input("Enter your age: "))

tax = 0

# checking exemption limit based on age
if age >= 60:
    exemption_limit = 300000
else:
    exemption_limit = 250000

# tax calculation
if income <= exemption_limit:
    tax = 0

elif income <= 500000:
    tax = (income - exemption_limit) * 0.05

elif income <= 1000000:
    tax = ((500000 - exemption_limit) * 0.05) + \
          ((income - 500000) * 0.20)

else:
    tax = ((500000 - exemption_limit) * 0.05) + \
          (500000 * 0.20) + \
          ((income - 1000000) * 0.30)

# displaying result
print("Total Tax Payable: Rs ", tax)