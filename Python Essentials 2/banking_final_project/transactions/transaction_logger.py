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

    def check_string_in_file(file_path, search_string):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if search_string in line:
                        print(f"Found '{search_string}' in line: {line.strip()}")
                    return True
            print(f"'{search_string}' not found in the file.")
            return False
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

