# Problem 40
# Print multiplication tables from 1 to 10

# Outer loop for numbers 1 to 10
for num in range(1, 11):
    # Print table heading
    print("Multiplication Table of", num)

    # Inner loop for multiplying from 1 to 10
    for i in range(1, 11):
        result = num * i
        # Multiply current number with i

        print(num, "x", i, "=", result)

    # Print blank line after each table
    print()