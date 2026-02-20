# Program to print right aligned star triangle

rows = 6   # Number of rows

for i in range(1, rows + 1):
    
    # Print spaces
    for space in range(rows - i):
        print("  ", end="")   # two spaces for proper alignment
    
    # Print stars
    for star in range(i):
        print("* ", end="")
    
    # Move to next line
    print()