"""
This is an application that uses classes in a simple bank app 
"""

class Account:
    def __init__(self, account_number, account_name, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        amount = int(input("Please enter deposit amount: "))
        return self.balance == self.balance + amount

    def withdrawal(self, amount):
        amount = int(input("Please enter withdrawal amount: "))
        return self.balance == self.balance - amount

    def get_balance(self):
        return f"Your current balance is GH {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_name, account_number, balance, interest_rate, interest_method):
        super().__init__(account_name, account_number, balance)
        self.interest_rate = interest_rate
        self.interest_method = interest_method

class CurrentAccount(Account):
    def __init__(self, account_name, account_number, balance, overdraft_limit, check_overdraft_method):
        super().__init__(account_name, account_number, balance)
        self.overdraft_limit = overdraft_limit
        self.check_overdraft_method = check_overdraft_method

class Bank:
    def __init__(self, account_list):
        self.account_list = account_list

    def add_account(self):
        pass

    def remove_account(self):
        pass

    def view_all_accounts(self):
        pass
