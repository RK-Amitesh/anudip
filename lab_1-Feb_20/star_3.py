# Program to print centered pyramid pattern using multiplication operator

rows = 5   # number of rows

for i in range(1, rows + 1):
    
    # Print spaces using multiplication
    print("  " * (rows - i), end="")
    
    # Print stars using multiplication
    print("* " * (2 * i - 1))