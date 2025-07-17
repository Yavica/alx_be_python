# finance_calculator.py

# Task: Calculate monthly savings and projected annual savings with interest.

# 1. User Input for Financial Details:
# Prompt the user for their monthly income.
# The 'input()' function gets text from the user.
# We then use 'float()' to convert that text into a floating-point number (a number with decimals),
# because income/expenses can have cents.
monthly_income_str = input("Enter your monthly income: ")
monthly_income = float(monthly_income_str)

# Ask for their total monthly expenses.
monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = float(monthly_expenses_str)

# 2. Calculate Monthly Savings:
# Subtract expenses from income to find the monthly savings.
monthly_savings = monthly_income - monthly_expenses

# 3. Project Annual Savings:
# Assume a simple annual interest rate of 5%.
annual_interest_rate = 0.05

# Calculate the projected savings after one year, incorporating the interest.
# Formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
# This can be simplified to: Monthly Savings * 12 * (1 + 0.05)
projected_annual_savings = monthly_savings * 12 * (1 + annual_interest_rate)

# 4. Output Results:
# Display the user’s monthly savings.
# Using an f-string for clear output. We use ':.2f' to format the number to two decimal places,
# which is common for currency.
print(f"Your monthly savings are ${monthly_savings:.2f}.")
1000
# Display the projected annual savings after including interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}")
