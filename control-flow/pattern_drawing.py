# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")  # Stay on the same line
    
    print()  # Move to the next line
    row += 1
