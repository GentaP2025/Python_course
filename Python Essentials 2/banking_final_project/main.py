from models.customer import Customer
from models.manager import Manager
from accounts.bank_account import BankAccount
from transactions.transaction_logger import TransactionLogger
from datetime import datetime
from utils.file_handler import save_customers
from utils.file_handler import load_customers

def main():
    cust1 = Customer("Ana", "ana@gmail.com","0001")

    acc1 = BankAccount("001","0001")
    acc2 = BankAccount("002","0001")
    
    cust1.add_account("001")
    cust1.add_account("002")

    log1 = TransactionLogger()
    if TransactionLogger.check_string_in_file("data/customers.csv", cust1.cus_ID):
        print("Customer exists")
    else:
        log1.log_customer(cust1.name, cust1.email,cust1.cus_ID,cust1.bank_acc)
        print (f"{cust1.cus_ID} added to customer file" )

    acc1.deposit(200)
    log1.log_transaction((datetime.now()).strftime("%y/%B/%d %H:%M:%S"),"Ana","00001","deposit",200)
    acc2.withdraw(100)
    log1.log_transaction((datetime.now()).strftime("%y/%B/%d %H:%M:%S"),"Ana","00001","withdraw",100)
    
    cust2 = Customer("Besi", "Besi@gmail.com","0002")
    
    acc3 = BankAccount("003","0002")
    acc4 = BankAccount("004","0002",1000)
    
    cust2.add_account("003")
    cust2.add_account("004")    

    log2 = TransactionLogger()
    if TransactionLogger.check_string_in_file("data/customers.csv", cust2.cus_ID):
        print("Customer exists")
    else:
        log2.log_customer(cust2.name, cust2.email,cust2.cus_ID,cust2.bank_acc) 
        print (f"{cust2.cus_ID} added to customer file" )

    
    acc3.deposit(350)
    log2.log_transaction((datetime.now()).strftime("%y/%B/%d %H:%M:%S"),"Besi","00002","deposit",350)

    acc4.withdraw(400)
    log2.log_transaction((datetime.now()).strftime("%y/%B/%d %H:%M:%S"),"Besi","00002","withdraw",400)

    print(acc1.display_info())
    print(acc2.display_info())
    print(acc3.display_info())
    print(acc4.display_info())

  
    man1 = Manager("M1","Bob")
    man1.m_view_logs()
    man1.view_customer([cust1,cust2])

    #Testing json
    customers = [cust1,cust2]
    save_customers (customers, 'data/customers.json')

    customers = load_customers('data/customers.json')
    for customer in customers:
        print("Testing json:", customer.name, customer.email)

if __name__ == "__main__":

    main()
