rows = 5  # Number of rows for the pyramid

for row in range(1, rows + 1):
    # Print leading spaces
    for col in range(rows - row):
        print(" ", end=" ")
    
    # Print stars
    for col in range(1, row + 1):
        print("* ", end="")
    
    # Move to the next line after each row
    print()
