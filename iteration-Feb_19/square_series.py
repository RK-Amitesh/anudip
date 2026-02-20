# Square Number Series
# Program to print square numbers up to 2500
# Series: 1, 4, 9, 16, 25, ...
# Logic: Difference between squares is consecutive odd numbers (3, 5, 7, 9...)

x = 1      # First square number (1^2)
y = 3      # First difference

# Loop until square reaches 2500
while x <= 2500:
    print(x)
    x = x + y      # Add current difference
    y = y + 2      # Increase difference by 2 (next odd number)