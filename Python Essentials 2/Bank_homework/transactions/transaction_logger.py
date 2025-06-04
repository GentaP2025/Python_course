class TransactionLogger:
    def __init__(self):
        pass

    def log_transaction(self,customer_name, action, amount:int):
        with open("data/transaction_log.txt", "a") as file:
            file.write(f"{customer_name} | {action} | {amount}\n")

