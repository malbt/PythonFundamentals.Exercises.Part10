from typing import Dict
from persistent_small_town_teller import PersistenceUtils


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
    def __init__(self, acc_number, acc_type, acc_owner, balance=0):
        self.acc_number = acc_number
        self.acc_type = acc_type
        self.acc_owner = acc_owner
        self.balance = balance

    def __repr__(self):
        return f'{self.acc_number}, {self.acc_type}, {self.acc_owner}, {self.balance}'


class Bank:
    def __init__(self):
        self.customer: Dict[int, Person] = Dict()
        self.account : Dic[int, Account] = Dict()

    def add_customer(self, customer:Person) -> None:
        if customer_id in self.customer:
            raise ValueError(f"{customer_id} already exists")
        else:
            self.customer[customer_id] = customer

    def add_account(self, account:Acoount):
        if account.customer_id not in self.customer:
            raise ValueError(f"{account.customer_id} not valid customer_id")
        elif account.acc_number in self.account:
            raise ValueError(f"{account.acc_number} already exists")
        else:
            self.account[account.acc_number] = account

    def delete_account(self, acc_number:int):
        if acc_number in self.account:
            del self.account[acc_number]
        else:
            raise ValueError(f"{account.acc_number} do not exist")

    def deposit(self, acc_number, amount):
        self.account[acc_number] += amount
        print("Deposit :", amount)

    def withdrawal(self, acc_number, amount):
        if self.account[acc_number] >= amount:
            print("Withdrawal : ", amount)
        else:
            raise ValueError (f"Transaction declined {account.acc_number}  not enough amount")

    def balance_inquiry(self, acc_number):
        print(f'Account Balance = {self.account[acc_number]}')

    def save_data(self):
        PersistenceUtils.write_pickle("customer.pickle", self.customer)
        PersistenceUtils.write_pickle("account.pickle", self.account)

    def load_data(self):
        self.customer = PersistenceUtils.load_pickle("customer.pickle")
        sel.account = PersistenceUtils.load_pickle("account.pickle")


