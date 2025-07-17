# multiplication_table.py

# Task 2: Multiplication Table Generator
# Objective: Use a for loop to generate and print the multiplication table for a given number.

# 1. Prompt User for a Number:
# We use int() to convert the user's input string into an integer.
# A try-except block is used to gracefully handle cases where the user might
# enter non-numeric input, preventing the program from crashing.
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit() # Exit the script if the input is not a valid integer

# 2. Generate and Print the Multiplication Table:
# The 'for' loop is ideal here because we know exactly how many times we need to iterate
# (from 1 to 10).
# range(1, 11) generates a sequence of numbers starting from 1 up to (but not including) 11.
# So, it will produce 1, 2, 3, ..., 10.
for i in range(1, 11):
    # Calculate the product of the user's number and the current iterator 'i'.
    product = number * i
    # Print each line of the multiplication table in the specified format.
    # An f-string (formatted string literal) is used for easy embedding of variables.
    print(f"{number} * {i} = {product}")

# This task demonstrates the power of 'for' loops in automating repetitive calculations
# and output, making the code concise and efficient for generating sequences.
