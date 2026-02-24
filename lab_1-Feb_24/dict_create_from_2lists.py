# Problem 84
# Create dictionary from two lists

keys = input("Enter keys separated by space: ").split()
values = list(map(int, input("Enter values separated by space: ").split()))

# zip() pairs elements from both lists
result = dict(zip(keys, values))

print("Created dictionary:", result)