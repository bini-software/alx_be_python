# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for rows
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print '*' in a row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
