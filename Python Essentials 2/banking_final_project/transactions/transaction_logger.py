from os import strerror
import os


class TransactionLogger:
    def log_transaction(self,date, customer_name, action, amount:int):
        try:
            with open("data/transaction_log.txt", "a") as file:
                file.write(f"{date} |{customer_name} | {action} | {amount}\n")

        except Exception as exc:
            print("The file could not be opened:", strerror(exc.errno))

    def log_customer(self,name,email,cust_ID, bank_acc):
        try:
                with open("data/customers.csv", "a") as file:
                    file.write(f"{name} |{email} | {cust_ID} | {bank_acc}\n")

        except Exception as exc:
            print("The file could not be opened:", strerror(exc.errno))

        except Exception as e:
            print(f"An error occurred: {e}")