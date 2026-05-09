# Q19. Write a function that accepts a list
# of integers and returns a new list containing
# factorial of only even numbers.

def factorial(num):

    fact = 1

    for i in range(1, num + 1):

        fact = fact * i

    return fact


def even_factorial(list1):

    new_list = []

    for i in list1:

        # checking even number
        if i % 2 == 0:

            new_list.append(factorial(i))

    return new_list


numbers = []

n = int(input("How many numbers you want to enter : "))

for i in range(n):

    value = int(input("Enter number : "))
    numbers.append(value)

result = even_factorial(numbers)

print("\nFactorial of Even Numbers :")
print(result)