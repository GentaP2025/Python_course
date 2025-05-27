class BankSystem:

    def __init__(self):
        self.accounts = []        

    def add_account(self,account):
        self.accounts.append(account)

    #def show_all_accounts(self):
        #return self.accounts
    
    def show_all_accounts(self):
        for account in self.accounts:
            print(account)    
    

    def find_account_by_number(self,acc_number):
        for account in self.accounts:
            if str(acc_number) == account:
                return acc_number
        print("Account number do not exist")
    

    def log_transaction(self,account_number,transaction):
        print(f"Transaction for account {account_number}: {transaction}")     

