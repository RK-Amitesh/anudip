# Program to:
# 1. Create a list of 20 numbers
# 2. Ask the user to enter a number
# 3. Remove all occurrences of that number
#    except for its first occurrence


# -------------------------------
# Step 1: Create a list of 20 numbers
# -------------------------------

numbers = []

print("Enter 20 numbers:")

# Loop runs 20 times to take input from user
for i in range(20):
    num = int(input("Enter number: "))
    numbers.append(num)   # Adding number to list

print("\nOriginal List:", numbers)


# -------------------------------
# Step 2: Ask user for the number to modify
# -------------------------------

target = int(input("\nEnter the number to remove duplicates of (except first occurrence): "))


# -------------------------------
# Step 3: Remove all occurrences except first
# -------------------------------

if target in numbers:
    
    first_index = numbers.index(target)
    # index() gives the position of first occurrence

    count = 0   # Counter to track occurrences

    new_list = []   # Creating a new list

    for i in range(len(numbers)):
        
        if numbers[i] == target:
            count += 1
            
            if count == 1:
                # Keep the first occurrence
                new_list.append(numbers[i])
            # Do nothing for other occurrences (skip them)
        
        else:
            # Add all other numbers normally
            new_list.append(numbers[i])

    print("\nUpdated List:", new_list)

else:
    print("\nNumber not found in the list.")