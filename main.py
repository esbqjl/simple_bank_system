
import argparse
from bank import BankSystem

def main():
    # Initialize BankSystem
    bank = BankSystem()

    # Create an ArgumentParser object with a description
    parser = argparse.ArgumentParser(
        description="Banking System: A simple command-line banking system where users can create accounts, deposit, withdraw, transfer, and check balances."
    )

    # Define expected arguments
    parser.add_argument('--account', type=str, help='Account ID (e.g., "1234567890123456")')
    parser.add_argument('--password', type=str, help='Password for the account (e.g., "mypassword")')
    parser.add_argument('--create', action='store_true', help='Create a new account')
    parser.add_argument('--deposit', type=float, help='Deposit amount (e.g., 100.50)')
    parser.add_argument('--withdraw', type=float, help='Withdraw amount (e.g., 50.00)')
    parser.add_argument('--transfer', type=float, help='Transfer amount (e.g., 200.00)')
    parser.add_argument('--to', type=str, help='Recipient account for transfer (e.g., "1234567890123456")')
    parser.add_argument('--balance', action='store_true', help='Check balance of an account')
    parser.add_argument('--change-password', action='store_true', help='Change the account password')

    # Parse arguments
    args = parser.parse_args()

    # Handle account creation
    if args.create:
        print("Creating a new account...")
        account_id = bank.create_account()  # Balance defaults to 0
        print(f"Account created with ID: {account_id}")

    # Handle deposit
    elif args.deposit and args.account and args.password:
        print(f"Depositing ${args.deposit:.2f} to account {args.account}.")
        if bank.verify_password(args.account, args.password):
            bank.deposit(args.account, args.deposit)
        else:
            print("Invalid password.")

    # Handle withdrawal
    elif args.withdraw and args.account and args.password:
        print(f"Withdrawing ${args.withdraw:.2f} from account {args.account}.")
        if bank.verify_password(args.account, args.password):
            bank.withdraw(args.account, args.withdraw)
        else:
            print("Invalid password.")

    # Handle transfer
    elif args.transfer and args.account and args.password and args.to:
        print(f"Transferring ${args.transfer:.2f} from account {args.account} to account {args.to}.")
        if bank.verify_password(args.account, args.password):
            bank.transfer(args.account, args.to, args.transfer)
        else:
            print("Invalid password.")

    # Check balance
    elif args.balance and args.account and args.password:
        if bank.verify_password(args.account, args.password):
            bank.get_balance(args.account)
        else:
            print("Invalid password.")

    # Handle password change
    elif args.change_password and args.account and args.password:
        print(f"Changing password for account {args.account}.")
        bank.change_password(args.account, args.password)

    else:
        print("Invalid arguments or missing required arguments.")

    # Save accounts state to CSV after operations
    bank.save_accounts()

if __name__ == "__main__":
    main()
