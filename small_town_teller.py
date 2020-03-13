class Person:
    def __init__(self, per_id, first_name, last_name):
        Person.per_id = ''  # PK
        Person.first_name = ''
        Person.last_name = ''


class Account:
    def __init__(self, acc_number, acc_type, acc_owner, acc_balance):
        Account.acc_number = ''  # PK
        Account.acc_type = ''
        Account.owner = ''  # not null or already in person
        Account.acc_balance = ''


# Declare a Bank class able to support the following operations:
#
# Adding a customer to the bank
# Adding an account to the bank
# Removing an account from the bank
# Depositing money into an account
# Withdrawing money from an account
# Balance inquiry for a particular account


def withdraw():
    amount = float(input("Enter amount to Withdraw: "))


class Bank:
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def deposit(self):
        amount = float(input("Enter deposit: "))

        self.balance += amount

        print("Amount Deposited:", amount)

        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal: ", amount)
        else:
            print("Insufficient balance  ")

    def balance_inquiry(self):
        print("Available Balance : ", self.balance)
