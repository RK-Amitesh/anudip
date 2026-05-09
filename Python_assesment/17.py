# Q17. Create a program that checks whether
# numbers entered by the user are Armstrong
# numbers using loops and conditional statements.

num = int(input("Enter a number : "))

temp = num
sum = 0

# counting digits
digits = len(str(num))

# calculating Armstrong value
while temp > 0:

    rem = temp % 10

    sum = sum + (rem ** digits)

    temp = temp // 10

# checking Armstrong number
if sum == num:

    print(num, "is an Armstrong Number")

else:

    print(num, "is Not an Armstrong Number")