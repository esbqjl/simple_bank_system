import hashlib

class Account:
    def __init__(self, account_id, balance, password_hash):
        self.account_id = account_id
        self.balance = float(balance)
        self.password_hash = password_hash  # Store the hashed password
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f'Account ID: {self.account_id} | Balance: ${self.balance:.2f}'
    
    def to_csv(self):
        return [self.account_id, str(self.balance), self.password_hash]  # Ensure to use account_id
    
    @staticmethod
    def from_csv(data):
        return Account(data[0], data[1], data[2])  # Ensure to use account_id
    
    @staticmethod
    def hash_password(password):
        # Hash the password using SHA-256
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

