# Problem 7
# Convert temperature from Fahrenheit to Celsius

# Taking temperature in Fahrenheit from user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
# input() takes value as string
# float() converts it into decimal number
# Value stored in variable 'fahrenheit'

# Applying conversion formula
celsius = (fahrenheit - 32) * 5/9
# First subtract 32 from Fahrenheit value
# Then multiply the result by 5/9
# Store final value in variable 'celsius'

# Printing the result
print("Temperature in Celsius =", celsius)