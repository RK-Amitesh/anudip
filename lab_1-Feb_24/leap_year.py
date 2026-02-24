# Problem 11
# Check whether a given year is a leap year

# Taking year as input from user
year = int(input("Enter a year: "))
# Convert input string into integer
# Store in variable 'year'

# Applying leap year condition

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    # Condition 1:
    # Year divisible by 4 AND not divisible by 100
    # OR
    # Condition 2:
    # Year divisible by 400
    print("It is a Leap Year.")

else:
    # If above condition is False
    print("It is NOT a Leap Year.")