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


class Bank:

    def __init__(self):
        self.list_of_accounts = []

    def add_account(self, Account):
        self.list_of_accounts.append(Account)


    def remove_account(self, Account):
        self.list_of_accounts.remove(Account)

    def view_all_accounts(self):
        for account in self.list_of_accounts:
            print(account)


kofi = Account("101", "Kofi")
ama = SavingsAccount("102", "Ama", 5)
kwame = CurrentAccount("103", "kwame", 2000)
#ama.deposit()
#ama.withdraw()
#ama.get_balance()

adb1 = Bank()
adb1.add_account(ama)
adb1.add_account(kofi)
adb1.add_account(kwame)
adb1.view_all_accounts()

print(kofi.account_name, kofi.account_number)
print(f"Name is {ama.account_name}, Number: {ama.account_number}, int. rt: {ama.interest_rate}")
