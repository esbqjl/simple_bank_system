
import random
from account import Account
from tools.utils import save_accounts_to_csv, load_accounts_from_csv

class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.load_accounts()

    def generate_account_id(self):
        # Generate a 16-digit random number
        return str(random.randint(10**15, 10**16 - 1))

    def create_account(self, balance=0):
        # Generate a unique 16-digit account ID
        account_id = self.generate_account_id()

        # Check if the account ID already exists, if so, regenerate
        while account_id in self.accounts:
            account_id = self.generate_account_id()

        # Prompt user for a password and verify it
        password = self.get_password_input()

        # Hash the password before saving
        password_hash = Account.hash_password(password)

        # Create and store the new account with the hashed password
        account = Account(account_id, balance, password_hash)
        self.accounts[account_id] = account
        print(f"Account created with ID {account_id} and balance ${balance:.2f}.")
        return account_id

    def get_password_input(self):
        """Ask the user to input and verify the password."""
        password = input("Enter your password: ")
        password_verify = input("Verify your password: ")

        if password == password_verify:
            return password
        else:
            print("Passwords do not match. Please try again.")
            return None  # Returning None simulates failure, or you could handle it differently.


    def verify_password(self, account_id, password):
        account = self.get_account(account_id)
        if account:
            # Compare the hashed password with the stored hash
            return account.password_hash == Account.hash_password(password)
        return False

    def change_password(self, account_id, old_password):
        # Verify old password
        account = self.get_account(account_id)
        if account and self.verify_password(account_id, old_password):
            # If the old password is correct, prompt for the new password
            print("Enter your new password:")
            new_password = self.get_password_input()

            # Hash the new password and update it
            new_password_hash = Account.hash_password(new_password)
            account.password_hash = new_password_hash
            print(f"Password for account {account_id} has been successfully changed.")
        else:
            print("Old password is incorrect.")

    def deposit(self, account_id, amount):
        account = self.get_account(account_id)
        if account and account.deposit(amount):
            print(f"${amount:.2f} deposited into account {account_id}.")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, account_id, amount):
        account = self.get_account(account_id)
        if account and account.withdraw(amount):
            print(f"${amount:.2f} withdrawn from account {account_id}.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")
    
    def transfer(self, sender_id, receiver_id, amount):
        sender = self.get_account(sender_id)
        receiver = self.get_account(receiver_id)
        if sender and receiver and sender.transfer(amount, receiver):
            print(f"${amount:.2f} transferred from account {sender_id} to account {receiver_id}.")
        else:
            print("Invalid transfer.")

    def get_balance(self, account_id):
        account = self.get_account(account_id)
        if account:
            print(f"Account {account_id} balance: ${account.get_balance():.2f}")
    
    def get_account(self, account_id):
        return self.accounts.get(account_id, None)
    
    def load_accounts(self):
        self.accounts = load_accounts_from_csv()

    def save_accounts(self):
        save_accounts_to_csv(self.accounts)

    def display_accounts(self):
        if self.accounts:
            for account in self.accounts.values():
                print(account)
        else:
            print("No accounts available.")
