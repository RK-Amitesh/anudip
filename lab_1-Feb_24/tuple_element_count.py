# Problem 69
# Count occurrence of element in tuple

# Taking tuple input
numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Taking element to search
element = int(input("Enter element to count: "))

# Initialize counter
count = 0

# Loop through tuple
for num in numbers:
    if num == element:
        count += 1
        # Increase counter if match found

# Print result
print("Element", element, "appears", count, "times")