# utils.py
import csv
from account import Account

def save_accounts_to_csv(accounts):
    with open('accounts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for account in accounts.values():
            writer.writerow(account.to_csv())

def load_accounts_from_csv():
    accounts = {}
    try:
        with open('accounts.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                account = Account.from_csv(row)
                accounts[account.account_id] = account
    except FileNotFoundError:
        print("No saved accounts found, starting fresh.")
    return accounts
