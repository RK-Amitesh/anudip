# Program to print right aligned star triangle

rows = 6   # Number of rows

for i in range(1, rows + 1):
    
    print("  "*(rows-i), end="")   # two spaces for proper alignment
    
    # Print stars
    print("* "*i, end="")
    
    # Move to next line
    print()