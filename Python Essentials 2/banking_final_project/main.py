from models.customer import Customer
from models.manager import Manager
from accounts.bank_account import BankAccount
from transactions.transaction_logger import TransactionLogger

def main():
    cust1 = Customer("Ana", "ana@gmail.com","0001",["001","002"])
    log1 = TransactionLogger()
    if TransactionLogger.check_string_in_file("data/customers.csv", cust1.cus_ID):
        print("Customer exists")
    else:
        log1.log_customer(cust1.name, cust1.email,cust1.cus_ID,cust1.bank_acc)
        print (f"{cust1.cus_ID} added to customer file" )

    acc1 = BankAccount("001","0001")
    acc2 = BankAccount("002","0001")

    acc1.deposit(200)
    log1.log_transaction("2025/06/16","Ana","00001","deposit",200)
    acc2.withdraw(100)
    log1.log_transaction("2025/06/16","Ana","00001","withdraw",100)
    print(acc1.display_info())
    print(acc2.display_info())

    cust2 = Customer("Besi", "Besi@gmail.com","0002",["003","004"])
    log2 = TransactionLogger()
    if TransactionLogger.check_string_in_file("data/customers.csv", cust2.cus_ID):
        print("Customer exists")
    else:
        log2.log_customer(cust2.name, cust2.email,cust2.cus_ID,cust2.bank_acc) 
        print (f"{cust2.cus_ID} added to customer file" )

    acc3 = BankAccount("003","0002")
    acc4 = BankAccount("004","0002",1000)

    acc3.deposit(350)
    log2.log_transaction("2025/06/16","Besi","00002","deposit",350)
    acc4.withdraw(400)
    log2.log_transaction("2025/06/16","Besi","00002","withdraw",400)
    print(acc3.display_info())
    print(acc4.display_info())

    man1 = Manager("M1","Bob")
    print(Manager.m_view_logs())

    man1.view_customer([cust1,cust2])

if __name__ == "__main__":

    main()
