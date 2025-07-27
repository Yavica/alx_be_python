# fns_and_dsa/explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now() # Get the current date and time
    # Format the datetime object into a string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date # Return the datetime object for further use if needed

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates a future date.
    Displays the future date in 'YYYY-MM-DD' format.
    """
    while True:
        try:
            days_to_add_str = input("Enter the number of days to add to the current date: ").strip()
            days_to_add = int(days_to_add_str) # Convert input to an integer
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter a whole number for days.")

    # Get the current date (without time for simpler future date calculation)
    # Or you can reuse the current_date from display_current_datetime if you called it first
    current_date_only = datetime.now().date() 
    
    # Calculate the future date by adding the timedelta
    future_date = current_date_only + timedelta(days=days_to_add)
    
    # Format the future date into a string
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date # Return the date object for further use if needed

# Main execution block
if __name__ == "__main__":
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate a future date
    calculate_future_date()