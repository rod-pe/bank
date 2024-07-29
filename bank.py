import random

class Account:
    def __init__(self, num):
        self.number = num
        self.amount = 0.0

    def deposit(self, amnt):
        if amnt > 0:
            self.amount += amnt
            print("Deposited {:.2f}, new balance is {:.2f}".format(amnt, self.amount))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amnt):
        if amnt > 0:
            if self.amount >= amnt:
                self.amount -= amnt
                print("Withdrew {:.2f}, new balance is {:.2f}".format(amnt, self.amount))
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def __str__(self):
        return "Account Number: {}, Balance: {:.2f}".format(self.number, self.amount)

# Example usage:
account_number = random.randint(1000, 99999)
account = Account(account_number)
print(account)

account.deposit(100)
account.withdraw(30)
account.withdraw(20)
account.withdraw(10)
print(account)
