# simple_interest.py

# Task: Calculate the simple interest earned on an investment.

# 1. Define three variables: principal, rate, and time.
# P is the principal amount (initial investment).
principal = 1000  # Represents $1000

# R is the annual interest rate (as a decimal).
# 0.05 represents 5% (5 / 100).
rate = 0.05

# T is the time the money is invested for in years.
time = 3  # Represents 3 years

# 2. Calculate the simple interest using the formula I = P * R * T.
# The result will be stored in a variable named 'interest'.
interest = principal * rate * time

# 3. Print the calculated interest in the specified format.
# Using an f-string to embed the 'interest' variable directly into the output string.
print(f"The simple interest is: {interest}")

