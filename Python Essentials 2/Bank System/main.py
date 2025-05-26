from system.account import BankAccount
from system.bank_system import BankSystem
from system.transaction import TransactionLog

acc1 = BankAccount("001", "Alice", 1000)
acc2 = BankAccount("002", "Bob", 500)
acc3 = BankAccount("003", "Mary", 2000)


bank = BankSystem([])
bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)

acc1.deposit(200)
bank.log_transaction("001", "Deposit $200")

acc2.withdraw(100)
bank.log_transaction("002", "Withdraw $100")

acc2.withdraw(400)
bank.log_transaction("003", "Withdraw $400")

bank.show_all_accounts()

# Print logs for account "001"
print(bank.log_transaction("001","Deposit $200"))

