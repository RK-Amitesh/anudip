# Problem 26
# Check whether a number is Armstrong

# Taking input from user
num = int(input("Enter a number: "))
# Convert input string to integer

# Store original number
original = num

# If number is negative, it cannot be Armstrong
if num < 0:
    print("Negative numbers cannot be Armstrong numbers.")

else:
    # Count number of digits
    temp = num
    count = 0

    while temp > 0:
        temp = temp // 10
        count += 1

    # If number is 0, it has 1 digit
    if original == 0:
        count = 1

    # Calculate Armstrong sum
    temp = num
    armstrong_sum = 0

    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** count
        temp = temp // 10

    # Check condition
    if armstrong_sum == original:
        print(original, "is an Armstrong number.")
    else:
        print(original, "is NOT an Armstrong number.")