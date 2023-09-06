'''
- Create a class for a `BankAccount` with a private attribute for balance and methods for deposit and withdrawal.
'''


class bankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.__balance = balance
        self.account_number = account_number

    def deposit(self, account_number, deposit_amount):
        self.__balance += deposit_amount
        print(f"Money {deposit_amount} is credited to {account_number}")

    def withdrawal(self, withdrawal_amount):
        if (self.__balance > withdrawal_amount):
            self.__balance -= withdrawal_amount
            print(
                f"Money {withdrawal_amount} is debited from {self.account_number}")
        else:
            print("Insufficient balance")

    def checking_balance(self):
        print(f"Money available in your account is {self.__balance}")


GokulsAccount = bankAccount("Gokul", 2000, 1234)
GokulsAccount.deposit(1234, 3000)
GokulsAccount.checking_balance()
