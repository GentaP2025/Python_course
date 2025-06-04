from os import strerror
import os


class TransactionLogger:
    def __init__(self):
        # Ensure the data directory exists
        if not os.path.exists("data"):
            os.makedirs("data")

    def log_transaction(self,customer_name, action, amount:int):
        try:
            with open("data/transaction_log.txt", "a") as file:
                file.write(f"{customer_name} | {action} | {amount}\n")

        except Exception as exc:
            print("The file could not be opened:", strerror(exc.errno))


