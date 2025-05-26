class BankAccount ():
    
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self):
        return f"Account Number: {self.account_number} | Holder: {self.account_holder} | Balance: ${self.balance:.2f}"
        
        
        
    
    
        
        
        
        
        


