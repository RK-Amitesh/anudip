# Problem 17
# Determine the type of triangle

# Taking three sides as input
a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
# float() used because sides may contain decimal values

# First check if it forms a valid triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    # Triangle inequality theorem satisfied

    # Now classify triangle based on sides

    if a == b and b == c:
        # All three sides equal
        print("It is an Equilateral Triangle.")

    elif a == b or b == c or a == c:
        # Any two sides equal
        print("It is an Isosceles Triangle.")

    else:
        # All sides different
        print("It is a Scalene Triangle.")

else:
    # If triangle inequality condition fails
    print("The given sides do NOT form a valid triangle.")