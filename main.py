# Project: SimpleBank_ATM
# Author: [Friend's Name/Matric Number]

class BankAccount:
    """
    Holds data for a single user account.
    Design Match: Class 'BankAccount'
    """
    def __init__(self, name, initial_money):
        self.acct_holder = name        # Matches Design: acct_holder
        self.balance = initial_money   # Matches Design: balance

class BankService:
    """
    Performs operations on BankAccounts.
    Design Match: Class 'BankService'
    """
    
    def process_deposit(self, account, amount):
        """
        Adds money to the account.
        Matches Design: process_deposit()
        """
        if amount > 0:
            account.balance += amount
            print(f"Alert: {amount} deposited successfully.")
        else:
            print("Error: Deposit amount must be positive.")

    def process_withdrawal(self, account, amount):
        """
        Deducts money if sufficient funds exist.
        Matches Design: process_withdrawal()
        """
        if amount > account.balance:
            print("Error: Insufficient funds!")
        else:
            account.balance -= amount
            print(f"Alert: {amount} withdrawn. Please take your cash.")

    def get_status(self, account):
        """
        Displays the current account state.
        Matches Design: get_status()
        """
        print(f"\n--- Statement for {account.acct_holder} ---")
        print(f"Current Balance: ${account.balance}")
        print("-----------------------------------\n")

# --- Execution Entry Point ---
if __name__ == "__main__":
    # Initialize the Service
    atm = BankService()

    # 1. Create an Account
    my_acct = BankAccount("John Doe", 1000)
    
    # 2. Check initial status
    atm.get_status(my_acct)

    # 3. Deposit Money
    atm.process_deposit(my_acct, 500)

    # 4. Withdraw Money
    atm.process_withdrawal(my_acct, 200)

    # 5. Fail Test (Withdraw too much)
    atm.process_withdrawal(my_acct, 5000)

    # 6. Final Status
    atm.get_status(my_acct)
