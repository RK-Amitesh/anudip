# Problem 81
# Find key with maximum value

# Example dictionary
data = {"A": 85, "B": 92, "C": 78, "D": 95}

# max(data, key=data.get)
# data.get returns value of each key
# max finds the key with highest value

max_key = max(data, key=data.get)

print("Key with maximum value:", max_key)
print("Maximum value:", data[max_key])