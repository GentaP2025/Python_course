class BankSystem:

    def __init__(self,accounts):
        self.accounts = []

    def add_account(self,account):
        self.accounts.append(account)

    def show_all_accounts(self):
        return print(self.accounts)
        
    

    def find_account_by_number(self,number):
        if str(number) in self.accounts:
            return number
        return print("Number do not exist")
    

    def log_transaction(self,account_number,transaction):
        print(account_number, transaction)

        

