"""
**Class and Objects:**
   - Implement a class for a simple bank account with methods for deposit, withdraw, and checking balance.

   - Create a class hierarchy for different types of vehicles (car, bike, truck) with shared and
   specific attributes/methods.


"""

class bankAccount:
    def __init__(self,name,balance,account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposit(self,account_number,deposit_amount):
        self.balance += deposit_amount
        print(f"Money {deposit_amount} is credited to {account_number}")

    def withdrawal(self,withdrawal_amount):
        if (self.balance>withdrawal_amount):
            self.balance -= withdrawal_amount
            print(f"Money {withdrawal_amount} is debited from {self.account_number}")
        else:
            print("Insufficient balance")


    def checking_balance(self):
        print(f"Money available in your account is {self.balance}")



GokulsAccount = bankAccount("Gokul",2000,1234)
GokulsAccount.deposit(1234,3000)
print(GokulsAccount.balance)
GokulsAccount.checking_balance()
GokulsAccount.withdrawal(300)
GokulsAccount.checking_balance()
GokulsAccount.withdrawal(50000)
GokulsAccount.checking_balance()

