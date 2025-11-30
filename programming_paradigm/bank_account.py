class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount with an optional initial balance.
        
        Args:
            initial_balance (float): Starting balance for the account. Defaults to 0.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        
        Args:
            amount (float): Amount to deposit into the account.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance if sufficient funds exist.
        
        Args:
            amount (float): Amount to withdraw from the account.
        
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
        """
        if amount > self.account_balance:
            return False
        elif amount > 0:
            self.account_balance -= amount
            return True
        else:
            print("Withdrawal amount must be positive.")
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")