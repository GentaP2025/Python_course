class BankSystem:

    def __init__(self):
        self.accounts = []        

    def add_account(self,account):
        self.accounts.append(account)

    def show_all_accounts(self):
        for account in self.accounts:
            print(account)    
    

    def find_account_by_number(self,acc_number:str):
        for account in self.accounts:
            if acc_number == account:
                return account
        print("Account number do not exist")
        return None

    def log_transaction(self,account_number,transaction):
        print(f"Transaction for account {account_number}: {transaction}")     

