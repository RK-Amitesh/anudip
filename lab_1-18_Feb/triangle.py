#check wether given 3 angles can form a triangle or not
a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))
if(a > 0 and b > 0 and c > 0):
    if(a + b + c == 180):
        print("The angles can form a triangle")
    else:
        print("The angles cannot form a triangle")
else:
    print("Invalid input. Angles must be greater than 0.")