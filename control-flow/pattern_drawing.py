# pattern_drawing.py

# Task 3: Drawing Patterns with Nested Loops
# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

# 1. Prompt User for Pattern Size:
# We use int() to convert the user's input to an integer.
# A try-except block is included for robust error handling in case of non-numeric input.
try:
    size = int(input("Enter the size of the pattern: "))
    # Basic validation: ensure the size is a positive integer
    if size <= 0:
        print("Please enter a positive integer for the pattern size.")
        exit() # Exit if input is not positive
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit() # Exit if input is not an integer

# 2. Draw the Pattern:
# We'll use a 'while' loop for the rows.
# 'row_count' will keep track of the current row we are printing.
row_count = 0
while row_count < size:
    # Inside the while loop, we use a 'for' loop for the columns (to print asterisks for each row).
    # The 'for' loop iterates 'size' number of times for each row.
    for _ in range(size):
        # print("*", end="") prints an asterisk without moving to the next line.
        # The 'end=""' argument tells print to use an empty string as the ending character
        # instead of the default newline character.
        print("*", end="")
    
    # After the inner 'for' loop completes (meaning a full row of asterisks has been printed),
    # print an empty string with the default newline to move to the next line.
    print()
    
    # Increment the row_count to move to the next row.
    row_count += 1

# This script effectively demonstrates nested loops: an outer 'while' loop controlling
# the rows, and an inner 'for' loop controlling the columns (printing characters)
# within each row. This pattern is common for working with 2D structures or grids.

