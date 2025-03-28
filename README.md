# Simple Banking System

A simple command-line banking system written in Python. This system allows users to create accounts, deposit and withdraw money, transfer funds, and check account balances. The system also supports secure password management by hashing the passwords before storing them. Additionally, users can change their passwords securely.

## Features

- **Create Account**: Users can create a new bank account with an initial balance.
- **Deposit Money**: Users can deposit money into their account.
- **Withdraw Money**: Users can withdraw money from their account (ensuring sufficient balance).
- **Transfer Funds**: Users can transfer money between accounts.
- **Check Balance**: Users can check the balance of their account.
- **Secure Passwords**: User passwords are securely hashed before being stored. Passwords can also be changed securely.

## Requirements

- Python 3.x
- `unittest` module for testing (Python's built-in module)

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/simple-banking-system.git
   cd simple-banking-system
   ```

Example Usage
1. Create a New Account
Use this command to create a new account. You will be prompted to enter and verify a password:


`python bank_system.py --create`

Sample output:

Enter your password: ********
Verify your password: ********
Account created with ID: 1234567890123456
2. Deposit Money into an Account
Use this command to deposit money into an account. Replace <account_id> and <your_password> with the account ID and the password you created earlier.

`python bank_system.py --account 1234567890123456 --password mypassword --deposit 100`

Sample output:

Depositing $100.00 to account 1234567890123456.
$100.00 deposited into account 1234567890123456.
3. Withdraw Money from an Account
Use this command to withdraw money from your account. Replace <account_id> and <your_password> with the correct values.


`python bank_system.py --account 1234567890123456 --password mypassword --withdraw 50`

Sample output:

Withdrawing $50.00 from account 1234567890123456.
$50.00 withdrawn from account 1234567890123456.
4. Transfer Money Between Accounts
To transfer money between two accounts, use the following command. Replace <account_id>, <receiver_account_id>, and <your_password> with the appropriate values.

`python bank_system.py --account 1234567890123456 --password mypassword --to 9876543210987654 --transfer 200`

Sample output:

Transferring $200.00 from account 1234567890123456 to account 9876543210987654.
$200.00 transferred from account 1234567890123456 to account 9876543210987654.
5. Check Balance of an Account
To check the balance of an account, use this command:


`python bank_system.py --account 1234567890123456 --password mypassword --balance`

Sample output:

Account 1234567890123456 balance: $1000.00
6. Change Account Password
To change your password, use the following command. You will be prompted to enter your old password and your new password twice for confirmation:

`python bank_system.py --account 1234567890123456 --password mypassword --change-password`

Sample output:

Enter your old password: ********
Enter your new password: ********
Verify your new password: ********
Password for account 1234567890123456 has been successfully changed.
Code Structure
bank_system.py: The main script that runs the banking system. It accepts user input from the command line to perform various banking operations.

bank.py: Contains the logic for managing the bank system, including creating accounts, handling deposits, withdrawals, transfers, and password management.

account.py: Defines the Account class, which represents an individual bank account with a balance and hashed password.

test_bank_system.py: Unit tests for the banking system, verifying functionality like account creation, password change, deposits, withdrawals, and transfers.
