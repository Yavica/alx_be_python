class BankAccount:
    """A simple BankAccount class to manage deposits, withdrawals, and display balance."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default is 0)."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Deposit the specified amount to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Invalid deposit amount. Must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account if sufficient balance is available."""
        if amount > self.__account_balance:
            return False
        elif amount < 0:
            print("Invalid withdrawal amount. Must be positive.")
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
