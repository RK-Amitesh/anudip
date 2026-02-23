# Triangular Number Series
# Program to print triangular numbers up to 100
# Differences increase by 1 each time (2, 3, 4, 5...)

x = 1      # First triangular number
y = 2      # Initial difference

while x <= 100:
    print(x)
    x = x + y      # Add current difference
    y = y + 1      # Increase difference by 1