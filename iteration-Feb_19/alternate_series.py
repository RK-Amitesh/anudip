# Alternating Sign Series
# Program to print series with alternating signs
# Series: 4, -8, 12, -16, 20, ...

x = 4          # Starting value
y = 4          # Increment value
sign = 1       # Sign control variable

while x <= 804:
    print(sign * x)      # Multiply by sign
    x = x + y            # Increase value by 4
    sign = sign * -1     # Change sign each iteration