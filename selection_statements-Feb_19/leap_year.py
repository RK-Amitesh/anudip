# Leap Year Check
# Program to check whether a year is leap year or not

# Input year
year = int(input("Enter a year: "))

# Checking leap year condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a Leap Year")
else:
    print("The year is NOT a Leap Year")