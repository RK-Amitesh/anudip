# Q37. Write a recursive function to calculate
# the sum of digits of a given number and
# compare it with iterative approach.

# recursive function
def recursive_sum(num):

    if num == 0:

        return 0

    else:

        return (num % 10) + recursive_sum(num // 10)


# iterative function
def iterative_sum(num):

    sum = 0

    while num > 0:

        rem = num % 10

        sum = sum + rem

        num = num // 10

    return sum


number = int(input("Enter a number : "))

# calling functions
rec_result = recursive_sum(number)

iter_result = iterative_sum(number)

print("\nSum using Recursive Method =", rec_result)

print("Sum using Iterative Method =", iter_result)