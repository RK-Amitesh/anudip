#check wether given 3 angles can form a triangle or not
angle_1 = int(input("Enter the first angle: "))
angle_2 = int(input("Enter the second angle: "))
angle_3 = int(input("Enter the third angle: "))
if(angle_1 > 0 and angle_2 > 0 and angle_3 > 0):
    if(angle_1 + angle_2 + angle_3 == 180):
        print("The angles can form a triangle")
    else:
        print("The angles cannot form a triangle")
else:
    print("Invalid input. Angles must be greater than 0.")