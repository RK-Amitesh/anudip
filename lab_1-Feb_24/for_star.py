# Problem 33
# Print star pattern using for loop

# Taking input from user
n = int(input("Enter number of rows: "))
# Convert input string to integer

# Outer loop controls number of rows
for i in range(1, n + 1):
    # Inner loop prints stars in each row
    for j in range(1, i + 1):
        # Print star without moving to next line
        print("*", end=" ")

    # After printing stars in one row,
    # move to next line
    print()