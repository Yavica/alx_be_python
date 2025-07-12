# future_age_calculator.py

# Task: Ask the user for their current age and calculate how old they will be in 2050.

# 1. Prompt the user to input their current age.
# The 'input()' function displays a message to the user and waits for them to type something,
# then returns whatever they typed as a string.
current_age_str = input("How old are you? ")

# 2. Convert the user's input (which is a string) to an integer (whole number).
# We need to convert it because arithmetic operations (+, -, *) only work with numbers, not strings.
# The 'int()' function attempts to convert a string to an integer.
current_age = int(current_age_str)

# 3. Calculate how old the user will be in the year 2050.
# The problem states to assume the current year is 2023, so 2050 is 27 years in the future.
years_to_add = 27
future_age = current_age + years_to_add

# 4. Print the user's age in 2050 in the specified format.
# Using an f-string to embed the 'future_age' variable directly into the output string.
print(f"In 2050, you will be {future_age} years old.")

