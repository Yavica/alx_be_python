# match_case_calculator.py

# Task 1: Simple Calculator with Match Case
# Objective: Learn to use Match Case statements for handling multiple operations.

# 1. Prompt for User Input:
# Use float() to convert the input to a floating-point number,
# allowing for decimal values in calculations.
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    # Handle cases where the user enters non-numeric input
    print("Invalid input. Please enter numbers only.")
    exit() # Exit the script if input is invalid

# Ask for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Variable to store the result of the calculation
result = None

# 2. Perform the Calculation Using Match Case:
# The 'match' statement evaluates the 'operation' variable.
# Each 'case' block specifies a pattern to match against 'operation'.
if operation == '+':
    # If 'operation' is '+', perform addition.
    result = num1 + num2
elif operation == '-':
    # If 'operation' is '-', perform subtraction.
    result = num1 - num2
elif operation == '*':
    # If 'operation' is '*', perform multiplication.
    result = num1 * num2
elif operation == '/':
    # If 'operation' is '/', handle division.
    # Ensure to handle the division by zero case gracefully.
    if num2 == 0:
        print("Cannot divide by zero.")
        # Set result to None or a specific error message to indicate failure
        result = "Error"
    else:
        result = num1 / num2
else:
    # If 'operation' does not match any of the above cases, this block is executed.
    print("Invalid operation. Please choose from +, -, *, /.")
    result = "Error"
# 3. Output the Result:
# Only print the result if a valid calculation was performed (i.e., result is not "Error").
if result != "Error" and result is not None:
    print(f"The result is {result}.")

# This script demonstrates how 'match-case' can provide a cleaner and more readable
# way to handle multiple conditional branches compared to long if-elif-else chains,
# especially when dealing with discrete values like operation symbols.
