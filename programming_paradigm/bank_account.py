class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance (default = 0)."""
        self.__account_balance = initial_balance   # True encapsulation - EXCELLENT!

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__account_balance += amount
            return True  # Success
        else:
            print("Deposit amount must be positive.")
            return False  # Failure

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.__account_balance:
            return False  # insufficient funds
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        """Return the current account balance (useful for testing)."""
        return self.__account_balance