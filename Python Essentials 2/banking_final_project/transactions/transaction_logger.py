import os

class TransactionLogger:
    def log_transaction(self, date, customer_name,customer_ID, action, amount: int):
        try:
            if not os.path.exists("data"):
                os.makedirs("data")
            with open("data/transaction_log.txt", "a") as file:
                file.write(f"{date} | {customer_name} | {customer_ID} | {action} | {amount}\n")
        except Exception as exc:
            print(f"An error occurred while logging transaction: {exc}")

    def log_customer(self, name, email, cust_ID, bank_acc):
        try:
            if not os.path.exists("data"):
                os.makedirs("data")
            with open("data/customers.csv", "a") as file:
                file.write(f"{name} | {email} | {cust_ID} | {bank_acc}\n")
        except Exception as exc:
            print(f"An error occurred while logging customer: {exc}")

    @staticmethod
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
        
    def view_logs(self):
        if not os.path.exists("data/transaction_log.txt"):
            print("No transaction logs found.")
            return 
        with open("data/transaction_log.txt", "r") as file:
            logs = file.readlines()
            for log in logs:
                print(log)

