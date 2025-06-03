from models.customer import Customer
from transactions.transaction_logger import TransactionLogger

def main():
    customer1 = Customer("Anna", "anna@email.com")
    log1 = TransactionLogger()

    print(customer1.display_info())

    print(customer1.deposit(150))
    log1.log_transaction(customer1.name, "Deposit", 150)

    print(customer1.withdraw(50))
    log1.log_transaction(customer1.name, "Withdraw", 50)

    print(customer1.withdraw(200))
    log1.log_transaction(customer1.name, "Withdraw", 200)

if __name__ == "__main__":

    main()
