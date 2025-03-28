import unittest
from bank import BankSystem
from account import Account
from unittest.mock import patch

class TestBankSystem(unittest.TestCase):

    def setUp(self):
        """Set up the test environment by initializing BankSystem and creating an account."""
        self.bank = BankSystem()
        # Create a sample account for testing purposes
        self.account_id = self.bank.create_account(1000)  # Create with an initial balance of 1000
        self.password = "securepassword123"
        self.bank.get_account(self.account_id).password_hash = Account.hash_password(self.password)

    def test_account_creation(self):
        """Test 1: Test account creation and balance."""
        print("Running Test 1: Test account creation and balance.")
        account = self.bank.get_account(self.account_id)
        self.assertIsNotNone(account)
        self.assertEqual(account.get_balance(), 1000)
        self.assertEqual(account.account_id, self.account_id)

    def test_password_hashing(self):
        """Test 2: Test that the password is properly hashed."""
        print("Running Test 2: Test that the password is properly hashed.")
        account = self.bank.get_account(self.account_id)
        self.assertNotEqual(account.password_hash, self.password)  # The password hash should not equal the plaintext password
        self.assertTrue(Account.hash_password(self.password) == account.password_hash)

    def test_deposit(self):
        """Test 3: Test depositing money into an account."""
        print("Running Test 3: Test depositing money into an account.")
        initial_balance = self.bank.get_account(self.account_id).get_balance()
        self.bank.deposit(self.account_id, 500)
        updated_balance = self.bank.get_account(self.account_id).get_balance()
        self.assertEqual(updated_balance, initial_balance + 500)

    def test_withdraw(self):
        """Test 4: Test withdrawing money from an account."""
        print("Running Test 4: Test withdrawing money from an account.")
        initial_balance = self.bank.get_account(self.account_id).get_balance()
        self.bank.withdraw(self.account_id, 200)
        updated_balance = self.bank.get_account(self.account_id).get_balance()
        self.assertEqual(updated_balance, initial_balance - 200)

    def test_withdraw_insufficient_balance(self):
        """Test 5: Test withdrawing more than the available balance (should fail)."""
        print("Running Test 5: Test withdrawing more than the available balance (should fail).")
        initial_balance = self.bank.get_account(self.account_id).get_balance()
        self.bank.withdraw(self.account_id, 1500)  # Exceeds available balance
        updated_balance = self.bank.get_account(self.account_id).get_balance()
        self.assertEqual(updated_balance, initial_balance)  # Balance should remain the same

    def test_transfer(self):
        """Test 6: Test transferring money between accounts."""
        print("Running Test 6: Test transferring money between accounts.")
        # Create another account
        receiver_account_id = self.bank.create_account(500)
        initial_sender_balance = self.bank.get_account(self.account_id).get_balance()
        initial_receiver_balance = self.bank.get_account(receiver_account_id).get_balance()

        # Transfer 300 from sender to receiver
        self.bank.transfer(self.account_id, receiver_account_id, 300)

        updated_sender_balance = self.bank.get_account(self.account_id).get_balance()
        updated_receiver_balance = self.bank.get_account(receiver_account_id).get_balance()

        self.assertEqual(updated_sender_balance, initial_sender_balance - 300)
        self.assertEqual(updated_receiver_balance, initial_receiver_balance + 300)

    def test_change_password(self):
        """Test 7: Test changing the password."""
        old_password = self.password
        new_password = "newsecurepassword123"
        
        # Provide the old password, new password, and new password for confirmation
        with patch('builtins.input', side_effect=[old_password, new_password, new_password]):
            self.bank.change_password(self.account_id, old_password)

        # Verify that the new password is correctly hashed and updated
        account = self.bank.get_account(self.account_id)
        self.assertNotEqual(account.password_hash, Account.hash_password(old_password))
        self.assertEqual(account.password_hash, Account.hash_password(new_password))

    def test_change_password_with_wrong_old_password(self):
        """Test 8: Test attempting to change password with the wrong old password."""
        print("Running Test 8: Test attempting to change password with the wrong old password.")
        wrong_old_password = "wrongpassword"
        new_password = "newsecurepassword123"
        
        with patch('builtins.input', side_effect=[wrong_old_password, new_password, new_password]):
            self.bank.change_password(self.account_id, wrong_old_password)

        # The password should not be changed because the old password was incorrect
        account = self.bank.get_account(self.account_id)
        self.assertEqual(account.password_hash, Account.hash_password(self.password))  # Password should remain the same

    def test_check_balance(self):
        """Test 9: Test checking the balance."""
        print("Running Test 9: Test checking the balance.")
        account = self.bank.get_account(self.account_id)
        self.assertEqual(account.get_balance(), 1000)

if __name__ == "__main__":
    unittest.main()
