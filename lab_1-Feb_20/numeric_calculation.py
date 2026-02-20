# Function to display sum of two numbers
def displaysum(a, b):
    print("Sum of", a, "and", b, "is:", a + b)


# Function to return sum of two numbers
def calculatesum(a, b):
    return a + b


# Function to display difference of two numbers
def displaydifference(a, b):
    print("Difference of", a, "and", b, "is:", a - b)


# Function to return difference of two numbers
def calculatedifference(a, b):
    return a - b


# Function to display product of two numbers
def displayproduct(a, b):
    print("Product of", a, "and", b, "is:", a * b)


# Function to return product of two numbers
def calculateproduct(a, b):
    return a * b


# Function to display quotient of two numbers
def displayquotient(a, b):
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("Quotient of", a, "and", b, "is:", a / b)


# Function to return quotient of two numbers
def calculatequotient(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b