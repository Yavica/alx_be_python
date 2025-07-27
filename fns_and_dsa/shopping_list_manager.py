# fns_and_dsa/shopping_list_manager.py

def display_menu():
    """Displays the main menu for the shopping list manager."""
    print("Shopping List Manager") # This line is specifically adjusted
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager application."""
    shopping_list = [] # Initialize an empty list to store shopping items

    while True:
        display_menu() # Show the menu to the user
        raw_choice = input("Enter your choice: ").strip() # Get raw input as string

        try:
            choice = int(raw_choice) # Attempt to convert to integer
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
            continue # Skip to the next iteration of the loop

        if choice == 1: # Now compare with integers
            # Add Item functionality
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item) # Add the item to the end of the list
                print(f"'{item}' added to the shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == 2: # Compare with integer
            # Remove Item functionality
            if not shopping_list: # Check if the list is empty first
                print("Shopping list is empty. Nothing to remove.")
                continue # Go back to the menu loop, skipping the rest of this iteration
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list: # Check if the item exists in the list
                shopping_list.remove(item_to_remove) # Remove the first occurrence of the item
                print(f"'{item_to_remove}' removed from the shopping list.")
            else:
                print(f"'{item_to_remove}' not found in the shopping list.")
        elif choice == 3: # Compare with integer
            # View List functionality
            if not shopping_list: # Check if the list is empty
                print("\nYour shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate to add numbers to items
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == 4: # Compare with integer
            # Exit functionality
            print("Goodbye!")
            break # Exit the while loop, ending the program
        else:
            # Handle invalid numerical choices (e.g., 5, 0, -1)
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()