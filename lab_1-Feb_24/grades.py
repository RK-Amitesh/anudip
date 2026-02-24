# Problem 12
# Assign grades based on marks

# Taking marks as input from user
marks = float(input("Enter marks (0-100): "))
# input() takes string value
# float() converts it to decimal number
# Stored in variable 'marks'

# Checking if marks are valid
if marks < 0 or marks > 100:
    # Marks should be between 0 and 100
    print("Invalid marks entered.")

# Assigning grades using if-elif ladder
elif marks >= 90:
    # If marks are 90 or above
    print("Grade: A")

elif marks >= 80:
    # If marks are between 80 and 89
    print("Grade: B")

elif marks >= 70:
    # If marks are between 70 and 79
    print("Grade: C")

elif marks >= 60:
    # If marks are between 60 and 69
    print("Grade: D")

elif marks >= 50:
    # If marks are between 50 and 59
    print("Grade: E")

else:
    # If marks are below 50
    print("Grade: F")