# Problem 1
# Swap two numbers without using a third variable

# Taking first number as input from user
a = int(input("Enter first number: "))
# Converts user input into integer and stores in variable 'a'

# Taking second number as input from user
b = int(input("Enter second number: "))
# Converts user input into integer and stores in variable 'b'

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

# Swapping logic without third variable

a = a + b
# Step 1: Add both numbers and store result in 'a'
# Now 'a' contains sum of original a and b

b = a - b
# Step 2: Subtract original b from new 'a'
# This gives original value of 'a'
# Now 'b' becomes original 'a'

a = a - b
# Step 3: Subtract new 'b' (original a) from new 'a'
# This gives original value of 'b'
# Now 'a' becomes original 'b'

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)