# Cube Number Series
# Program to print cube numbers up to 27000
# Series: 1, 8, 27, 64, ...
# Logic: Uses 3-variable progression
# Third difference of cubes is constant (6)

x = 1      # First cube (1^3)
y = 7      # First difference
z = 12     # Second difference

# Loop until cube reaches 27000
while x <= 27000:
    print(x)
    x = x + y      # Add first difference
    y = y + z      # Update first difference
    z = z + 6      # Third difference is constant (6)