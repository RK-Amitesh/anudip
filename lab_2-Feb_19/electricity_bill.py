# Electricity Bill Calculator

# taking inputs
units = float(input("Enter number of units consumed: "))
age = int(input("Enter your age: "))

bill = 0

# calculating bill based on slab
if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

# applying senior citizen discount
if age >= 60:
    discount = bill * 0.10
    bill = bill - discount
    print("Senior citizen discount applied (10%)")

print("Total Electricity Bill: Rs ", bill)