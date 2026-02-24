# Problem 70
# Check whether tuple elements are unique

# Taking tuple input
numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Assume elements are unique
is_unique = True

# Check for duplicates using nested loop
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            is_unique = False
            break
    if not is_unique:
        break

# Print result
if is_unique:
    print("All elements are unique.")
else:
    print("Tuple contains duplicate elements.")