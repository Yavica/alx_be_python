# weather_advice.py

# Task 0: Weather Recommendation Program
# Objective: Utilize conditional statements (if, elif, else) to guide program execution
#            based on user input regarding weather conditions.
# 1. Prompt User for Weather Input:
# The input() function displays a message to the user and waits for them to type something
# and press Enter. The entered text is returned as a string.
# .lower() is used to convert the user's input to all lowercase. This makes the
# comparison case-insensitive, so 'Sunny', 'sunny', or 'SUNNY' will all be treated
# the same as 'sunny'.
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# 2. Provide Clothing Recommendations using if, elif, and else:
# This section uses conditional statements to make decisions based on the 'weather' variable.

# 'if' statement: Checks the first condition.
if weather == "sunny":
    # If the 'weather' is exactly "sunny", this print statement is executed.
    print("Wear a t-shirt and sunglasses.")
# 'elif' (short for "else if") statement: Checks this condition ONLY if the preceding
# 'if' (or any previous 'elif') condition was False.
elif weather == "rainy":
    # If the 'weather' is "rainy", this print statement is executed.
    print("Don't forget your umbrella and a raincoat.")
# Another 'elif' statement for the "cold" condition.
elif weather == "cold":
    # If the 'weather' is "cold", this print statement is executed.
    print("Make sure to wear a warm coat and a scarf.")
# 'else' statement: This block is executed ONLY if NONE of the preceding 'if' or 'elif'
# conditions were True. It acts as a fallback for any unexpected input.
else:
    print("Sorry, I don't have recommendations for this weather.")

# This script effectively demonstrates how control flow allows a program to
# follow different paths of execution based on specific conditions, making it
# dynamic and responsive to user input.
