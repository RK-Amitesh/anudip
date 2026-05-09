# Q32. Write a Python program that validates
# user age for voting eligibility and handles
# invalid numeric and non-numeric inputs gracefully.

try:

    age = int(input("Enter your age : "))

    # checking negative age
    if age < 0:

        print("Age Cannot Be Negative")

    # checking voting eligibility
    elif age >= 18:

        print("You Are Eligible for Voting")

    else:

        print("You Are Not Eligible for Voting")

# handling non-numeric input
except ValueError:

    print("Please Enter Valid Numeric Age")

# handling other errors
except Exception as e:

    print("Error :", e)