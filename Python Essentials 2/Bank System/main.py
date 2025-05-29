from system.account import BankAccount
from system.bank_system import BankSystem
from system.transaction import TransactionLog

acc1 = BankAccount("001", "Alice", 1000)
acc2 = BankAccount("002", "Bob", 500)
acc3 = BankAccount("003", "Mary", 100)

trn1 = TransactionLog()
trn2 = TransactionLog()
trn3 = TransactionLog()

bank = BankSystem()
bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)


acc1.deposit(200)
trn1.record("001","Deposit $200")
acc1.deposit(115)
trn1.record("001","Deposit $115")
bank.log_transaction("001", "Deposit $200")
bank.log_transaction("001", "Deposit $115")

if acc2.withdraw(100) == True:
    trn2.record("002","Withdraw $100")
    bank.log_transaction("002", "Withdraw $100")

if acc3.withdraw(400) == True:    
    trn3.record("003","Withdraw $400")
    bank.log_transaction("003", "Withdraw $400")

bank.show_all_accounts()

acc_f =  bank.find_account_by_number("003")
if acc_f:
    print(acc_f)

# Print logs for account "001"
print(bank.log_transaction("001",trn1.get_all("001")))

print(trn1.__str__())



