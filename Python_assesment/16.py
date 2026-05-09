# Q16. Write a Python program using functions and loops
# to generate Fibonacci numbers up to N and store
# only even Fibonacci numbers in a list.

def fibonacci(n):

    a = 0
    b = 1

    even_list = []

    print("Fibonacci Series :")

    while a <= n:

        print(a, end=" ")

        # checking even fibonacci numbers
        if a % 2 == 0:
            even_list.append(a)

        c = a + b
        a = b
        b = c

    print("\n\nEven Fibonacci Numbers :")
    print(even_list)


num = int(input("Enter the limit : "))

fibonacci(num)