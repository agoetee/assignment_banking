"""
This is a bank application that does some bank services
"""
class Account:
    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = 50

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print(f"You have deposited ${amount}. Your balance is ${self.balance}")
    
    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))
        if amount < self.balance:
            self.balance -= amount
            print(f"You have withdrawn ${amount}. You balance is ${self.balance}")
        else:
            print("Your balance is insufficient for the transaction")

    def get_balance(self):
        print(f"Your account balance is ${self.balance}")

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.interest_rate

    def interest_method(self):
ac1 = Account(101,"Agoe" )
ac1.withdraw()