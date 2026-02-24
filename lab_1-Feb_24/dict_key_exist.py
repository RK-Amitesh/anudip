# Problem 83
# Check whether key exists in dictionary

data = {"name": "Amit", "age": 22, "city": "Delhi"}

key = input("Enter key to check: ")

# 'in' checks existence of key
if key in data:
    print("Key exists in dictionary.")
else:
    print("Key does NOT exist.")