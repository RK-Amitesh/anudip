# Problem 68
# Convert tuple to list

# Taking input from user
tuple_data = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

# Convert tuple to list
list_data = list(tuple_data)

# Print result
print("Tuple:", tuple_data)
print("Converted List:", list_data)