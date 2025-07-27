# Ask for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row count
row = 0

# Outer loop for each row
while row < size:
    # Inner loop for each column in the row
    for star in range(size):
        print("*", end="")  # Print stars on the same line
    print()  # Move to the next line after a row is printed
    row += 1
