import types


class Person:
    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.customer_id}, {self.first_name}, {self.last_name}'

    def __repr__(self):
        return f'{self.customer_id}, {self.first_name}, {self.last_name}'


class Account:
    def __init__(self, acc_number, acc_type, acc_owner, balance):
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.acc_owner = acc_owner
        self.balance = balance

    def __repr__(self):
        return f'{self.acc_number}, {self.acc_type}, {self.acc_owner}, {self.balance}'


class Bank:
    def __init__(self):
        self.customer = []
        self.account = {}

    def add_customer(self, person):
        if person.customer_id in self.customer:
            self.customer.append(person.customer_id)
        else:
            print("please register customer first!")

    def add_account(self, account):
        if account not in self.account:
            self.account[account.acc_number] = account.balance
        else:
            print("Account number already exists!")

    def deposit(self, acc_number, amount):
        self.account[acc_balance] += amount

    def withdraw(self, act_number, amount):
        if self.account[acc_number] >= amount:
            self.account[acc_bnumber] -= amount
        else:
            print("Transaction declined! ")

    def balance_inquiry(self, acc_number):
        print(f'Account Balance = {sel.account[account_number]}')


from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob, balance)
zc_bank.add_account(bob_savings)
zc_bank.balance_inquiry(1001)
# 0
zc_bank.deposit(1001, 256.02)
zc_bank.balance_inquiry(1001)
# 256.02
zc_bank.withdrawal(1001, 128)
zc_bank.balance_inquiry(1001)
# 128.02


# Traceback (most recent call last):
#   File "/Users/mtessema/PythonFundamentals.Exercises.Part10/small_town_teller.py", line 58, in <module>
#     from small_town_teller import Person, Account, Bank
#   File "/Users/mtessema/PythonFundamentals.Exercises.Part10/small_town_teller.py", line 63, in <module>
#     bob_savings = Account(1001, "SAVINGS", bob, balance)
# NameError: name 'balance' is not defin