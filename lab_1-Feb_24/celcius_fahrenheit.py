# Problem 6
# Convert temperature from Celsius to Fahrenheit

# Taking temperature in Celsius from user
celsius = float(input("Enter temperature in Celsius: "))
# input() takes string value
# float() converts it into decimal number
# Value stored in variable 'celsius'

# Applying conversion formula
fahrenheit = (celsius * 9/5) + 32
# First multiply Celsius by 9/5
# Then add 32 to the result
# Store final value in variable 'fahrenheit'

# Printing the result
print("Temperature in Fahrenheit =", fahrenheit)