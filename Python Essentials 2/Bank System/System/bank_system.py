class BankSystem:

    def __init__(self):
        self.accounts = {}        

    def add_account(self,account):
        self.accounts[account.account_number] = account

    def show_all_accounts(self):
        for account in self.accounts.values():
            print(account)    
    

    def find_account_by_number(self, acc_number: str):
        for account in self.accounts.values():  
            if acc_number == account.account_number: 
                return account
        print("Account number does not exist")
        return None  

    def log_transaction(self,account_number,transaction):
        print(f"Transaction for account {account_number}: {transaction}")     


