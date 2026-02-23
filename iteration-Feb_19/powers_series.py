# Powers of 2
# Program to print powers of 2 up to 1024
# Series: 1, 2, 4, 8, 16, ...

x = 1      # Initial value
y = 2      # Multiplication factor

while x <= 1024:
    print(x)
    x = x * y      # Multiply by 2 each time