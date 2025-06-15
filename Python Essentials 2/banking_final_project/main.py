from models.customer import Customer
from models.manager import Manager
from transactions.transaction_logger import TransactionLogger

def main():
    cust1 = Customer("Ana", "ana@gmail.com","0001",["001","002"])
    log1 = TransactionLogger()
    log1.log_customer("Ana", "ana@gmail.com","0001",["001","002"])

if __name__ == "__main__":

    main()

