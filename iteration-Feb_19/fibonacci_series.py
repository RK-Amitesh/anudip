# Fibonacci Series
# Program to print Fibonacci series up to 100
# Series: 0, 1, 1, 2, 3, 5, 8...

a = 0      # First number
b = 1      # Second number

while a <= 100:
    print(a)
    temp = a + b   # Next term
    a = b          # Shift values
    b = temp