from account import BankAccount
from bank_system import Banksystem
from transaction import TransactionLog

acc1 = BankAccount("001", "Alice", 1000)
acc2 = BankAccount("002", "Bob", 500)
acc3 = BankAccount("003", "Mary", 2000)


bank = BankSystem()
bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)