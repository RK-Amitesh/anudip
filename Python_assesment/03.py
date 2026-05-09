# Q3. Create a program that generates the first N prime numbers
# using a for loop and also calculates the sum and average
# of those prime numbers.

n = int(input("Enter how many prime numbers you want : "))

count = 0
num = 2
sum = 0

print("\nPrime Numbers are :")

while count < n:

    prime = True

    for i in range(2, num):

        if num % i == 0:
            prime = False
            break

    if prime == True:
        print(num)

        sum = sum + num
        count = count + 1

    num = num + 1

average = sum / n

print("\nSum of Prime Numbers =", sum)
print("Average of Prime Numbers =", average)