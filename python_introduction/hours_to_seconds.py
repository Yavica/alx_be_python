# hours_to_seconds.py

# Task: Convert a specific number of hours into seconds.

# 1. Define a variable named 'hours' and assign it a value.
# As per the instructions, we'll use hours = 2.
hours = 2

# 2. Calculate the number of seconds in the given hours.
# Remember: 1 hour = 60 minutes, 1 minute = 60 seconds.
# So, 1 hour = 60 * 60 = 3600 seconds.
seconds_in_an_hour = 3600
seconds = hours * seconds_in_an_hour

# 3. Store the result of the conversion in a variable named 'seconds'.
# (This was done in the previous line: seconds = hours * seconds_in_an_hour)

# 4. Print the result in the specified format.
# Using an f-string to embed the 'hours' and 'seconds' variables directly into the output string.
print(f"{hours} hour(s) is {seconds} seconds.")

