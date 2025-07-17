# daily_reminder.py

# Task 4: Personal Daily Reminder
# Objective: Create a simplified Python script that uses conditional statements,
#            Match Case, and loops to remind the user about a single,
#            priority task for the day based on time sensitivity.

# 1. Prompt for a Single Task:
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for consistent comparison
time_bound_input = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase

# Determine if the task is time-bound (boolean for easier conditional checks later)
is_time_bound = (time_bound_input == 'yes')

# Initialize the base reminder message
reminder_message = ""

# 2. Process the Task Based on Priority using if-elif-else:
# The if-elif-else statement helps to handle different priority levels cleanly.
if priority == 'high':
    reminder_message = f"'{task}' is a high priority task"
elif priority == 'medium':
    reminder_message = f"'{task}' is a medium priority task"
elif priority == 'low':
    reminder_message = f"'{task}' is a low priority task"
else: # Default case for invalid priority input
    reminder_message = f"'{task}' has an unknown priority"
    print("Warning: Invalid priority entered. Please use 'high', 'medium', or 'low'.")

# 3. Modify the Reminder based on Time Sensitivity:
# An if statement is used here to add the time-sensitive phrase if applicable.
if is_time_bound:
    # Append the time-sensitive phrase directly to the existing reminder message.
    reminder_message += " that requires immediate attention today!"
else:
    # For non-time-bound tasks, provide an alternative suggestion based on priority.
    # We use an elif chain here to provide more specific advice.
    if priority == 'low':
        reminder_message += ". Consider completing it when you have free time."
    elif priority == 'medium':
        reminder_message += ". You should aim to complete it today."
    elif priority == 'high':
        reminder_message += ". It is important to get this done today."

# 4. Provide a Customized Reminder:
print(f"\nReminder: {reminder_message}")

# This script demonstrates combining different control flow elements:
# - input() for gathering user data.
# - match-case for handling discrete priority levels.
# - if-else for time sensitivity and refining messages.
# It creates a simple, dynamic reminder system.
