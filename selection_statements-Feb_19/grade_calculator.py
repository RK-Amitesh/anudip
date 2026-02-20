# Grade Calculator
# Program to calculate grade based on marks

# Input marks
marks = int(input("Enter marks: "))

# Checking grade condition
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")