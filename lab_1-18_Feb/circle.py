# program to calculate area and circumference of a circle
# input of radius

radius = float(input("Enter the radius of the circle: "))

# validating whether the radius is valid or not
if(radius <= 0):
    print("Invalid radius")
    exit()   # exiting the program if radius is invalid
else:
    # defining value of pi
    pi = 3.14159
    
    # calculating area of circle
    area = pi * radius * radius
    
    # calculating circumference of circle
    circumference = 2 * pi * radius
    
    # displaying results
    print("Area of the circle is:", area)
    print("Circumference of the circle is:", circumference)