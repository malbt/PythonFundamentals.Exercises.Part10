from typing import Dict
import pickle
from persistent_small_town_teller import PersistenceUtils


class Person:
    def __init__(self, customer_id: int, first_name: str, last_name: str):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.customer_id},  {self.first_name}, {self.last_name}"

    def __repr__(self):
        return f"{self.customer_id}, {self.first_name}, {self.last_name}"


class Account:
    def __init__(self, acc_number: int, acc_type: str, acc_owner: Person):
        self.acc_number: int = acc_number
        self.acc_type: str = acc_type
        self.acc_owner = acc_owner
        self.balance = 0

    def __repr__(self):
        return f'{self.acc_number}, {self.acc_type}, {self.acc_owner}'


class Bank:
    def __init__(self):
        self.customer: Dict[int, Person] = dict()
        self.account: Dict[int, Account] = dict()

    def add_customer(self, customer: Person) -> None:
        if customer.customer_id not in self.customer:
            self.customer[customer.customer_id] = customer.first_name
        else:
            raise ValueError(f"Customer with id {customer.customer_id} already exist.")

    def add_account(self, account: Account):
        if account.acc_number in self.account:
            raise ValueError(f"{account.acc_number} already exists")
        else:
            self.account[account.acc_number] = account

    def delete_account(self, acc_number: int):
        if acc_number in self.account:
            del self.account[acc_number]
        else:
            raise ValueError(f"{account.acc_number} do not exist")

    def deposit(self, acc_number: int, amount: float):
        if acc_number in self.account:
            account = self.account.get(acc_number)
            account.balance += round(amount, 2)

    def withdrawal(self, acc_number, amount: float):
        if acc_number in self.account:
            account = self.account.get(acc_number)
            account.balance -= round(amount, 2)
            print("Withdrawal : ", amount)
        else:
            raise ValueError(f"Transaction declined {account.acc_number}  not enough amount")

    def balance_inquiry(self, acc_number):
        print(f'Account Balance = {self.account[acc_number]}')

    def save_data(self):
        PersistenceUtils.write_pickle("customer.pickle", self.customer)
        PersistenceUtils.write_pickle("account.pickle", self.account)

    def load_data(self):
        self.customer = PersistenceUtils.load_pickle("customer.pickle")
        sel.account = PersistenceUtils.load_pickle("account.pickle")


zc_bank = Bank()

john = Person(1, "John", "Smith")
zc_bank.add_customer(john)
adam = Person(2, "Adam", "Morgan")
zc_bank.add_customer(adam)
berry = Person(3, "Berry", "Mak")
zc_bank.add_customer(berry)
sara = Person(4, "Sara", "Ali")
zc_bank.add_customer(sara)
alice = Person(5, "Alice", "Fitz")
zc_bank.add_customer(alice)
simmons = Person(6, "Simmons", "Dante")
zc_bank.add_customer(simmons)

john_saving = Account(1001, "Saving", john)
zc_bank.add_account(john_saving)
adam_checking = Account(1002, "Checking", adam)
zc_bank.add_account(adam_checking)
berry_checking = Account(1003, "Checking", berry)
zc_bank.add_account(berry_checking)
sara_saving = Account(1004, "Saving", sara)
zc_bank.add_account(sara_saving)
alice_saving = Account(1005, "Saving", alice)
zc_bank.add_account(alice_saving)
simmons_saving = Account(1006, "Saving", simmons)
zc_bank.add_account(simmons_saving)

zc_bank.deposit(1001, 2561)
zc_bank.balance_inquiry(1001)

zc_bank.deposit(1002, 2565)
zc_bank.balance_inquiry(1002)

zc_bank.deposit(1003, 2656)
zc_bank.balance_inquiry(1003)

zc_bank.deposit(1004, 2562)
zc_bank.balance_inquiry(1004)

zc_bank.deposit(1005, 2056.02)
zc_bank.balance_inquiry(1005)

zc_bank.deposit(1006, 2560.02)
zc_bank.balance_inquiry(1006)

zc_bank.withdrawal(1001, 8128)
zc_bank.balance_inquiry(1001)
zc_bank.withdrawal(1002, 1282)
zc_bank.balance_inquiry(1002)
zc_bank.withdrawal(1003, 1288)
zc_bank.balance_inquiry(1003)
zc_bank.withdrawal(1004, 1828)
zc_bank.balance_inquiry(1004)
zc_bank.withdrawal(1005, 1281)
zc_bank.balance_inquiry(1005)
zc_bank.withdrawal(1006, 1286)
zc_bank.balance_inquiry(1006)
