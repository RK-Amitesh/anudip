# Q23. Write a program to print a pyramid
# pattern of numbers and calculate the sum
# of all numbers printed in the pattern.

n = int(input("Enter number of rows : "))

sum = 0

print("\nNumber Pyramid :\n")

for i in range(1, n + 1):

    for j in range(1, i + 1):

        print(j, end=" ")

        sum = sum + j

    print()

print("\nSum of all numbers =", sum)