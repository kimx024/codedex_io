"""
The Legend of Python: Intermediate
This code is part of Exercise 19: Wealth Manager
This exercise introduces setUp() and tearDown() with the umbrella theme being Testing
"""

import unittest
from wealth_manager import BankAccount

class TestBankAccount(unittest.TestCase):
    # Test if we set everything up correctly
    def setUp(self):
        self.account = BankAccount(100)

    # Protocol tearDown() function to remove the account
    def tearDown(self):
        self.account = None

    # Test if we set up the correct starting amount
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    # Test if we can deposit a positive amount and if it's correctly added up0
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    # Test if an error is raised when we don't deposit anything
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    # Test if an error is raised when we don't withdraw anything
    def test_withdraw_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(0)

    # Test if an error is raised when we deposit a negative amount
    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-40)

    # Test if we can withdraw money when we have enough money
    def test_positive_withdrawal(self):
      self.account.withdraw(50)
      self.assertEqual(self.account.balance, 50)

    # Test if an error is raised if we try to withdraw more money then in the account
    def test_too_much_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

if __name__ == '__main__':
    unittest.main()