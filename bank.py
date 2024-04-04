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
    def __init__(self, account_number, account_name, interest_rate):
        super().__init__(account_number, account_name)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Your balance after rate {self.interest_rate} is ${self.balance}")

class CurrentAccount(Account):
    def __init__(self, account_number, account_name, overdraft_limit):
        super().__init__(account_number, account_name)
        self.overdraft_limit = overdraft_limit

    def check_overdraft(self):
        if self.balance <= 0 and abs(self.balance) > self.overdraft_limit:
            print("You have exceeded your overdraft limit")
        else:
            print("You are within your overdraft limit")


ac1 = Account(101,"Agoe" )
ac1.withdraw()