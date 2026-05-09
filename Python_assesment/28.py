# Q28. Develop a menu-driven mathematical
# utility program using functions for factorial,
# prime checking, and Armstrong number checking.

# factorial function
def factorial(num):

    fact = 1

    for i in range(1, num + 1):

        fact = fact * i

    print("Factorial =", fact)


# prime number function
def prime(num):

    count = 0

    for i in range(1, num + 1):

        if num % i == 0:

            count = count + 1

    if count == 2:

        print(num, "is a Prime Number")

    else:

        print(num, "is Not a Prime Number")


# armstrong function
def armstrong(num):

    temp = num
    sum = 0

    digits = len(str(num))

    while temp > 0:

        rem = temp % 10

        sum = sum + (rem ** digits)

        temp = temp // 10

    if sum == num:

        print(num, "is an Armstrong Number")

    else:

        print(num, "is Not an Armstrong Number")


# menu-driven program
while True:

    print("\n----- Mathematical Utility Menu -----")
    print("1. Factorial")
    print("2. Prime Number Check")
    print("3. Armstrong Number Check")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        num = int(input("Enter a number : "))
        factorial(num)

    elif choice == 2:

        num = int(input("Enter a number : "))
        prime(num)

    elif choice == 3:

        num = int(input("Enter a number : "))
        armstrong(num)

    elif choice == 4:

        print("Exiting Program")
        break

    else:

        print("Invalid Choice")