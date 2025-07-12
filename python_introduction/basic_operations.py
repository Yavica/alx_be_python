# basic_operations.py

# Task: Perform basic arithmetic operations with two predefined numbers.

# 1. Assign specific values to two variables: number1 and number2.
# A variable is a named storage location for data.
# Here, we're assigning the integer value 10 to 'number1'.
number1 = 10
# And the integer value 5 to 'number2'.
number2 = 5

# 2. Perform addition, subtraction, and multiplication on these numbers.

# Addition: Use the '+' operator to sum the two numbers.
sum_result = number1 + number2

# Subtraction: Use the '-' operator to find the difference (number1 minus number2).
difference_result = number1 - number2

# Multiplication: Use the '*' operator to find the product.
product_result = number1 * number2

# 3. Print the results of these operations in a human-readable format.
# The 'print()' function displays output to the console.
# We use f-strings (formatted string literals) for easy formatting.
# F-strings start with 'f' or 'F' before the opening quote,
# and allow you to embed expressions inside curly braces {}.

# Print the addition result.
print(f"Addition of {number1} and {number2} is {sum_result}")

# Print the subtraction result.
print(f"Subtraction of {number1} and {number2} is {difference_result}")

# Print the multiplication result.
print(f"Multiplication of {number1} and {number2} is {product_result}")

