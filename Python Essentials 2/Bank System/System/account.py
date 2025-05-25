class BankAccount (self,account_number,account_holder,balance = 0.0):
    
    def __init__(self):
        account_number = account_number
        account_holder = account_holder
        balance = balance

    def deposit(self,amount):
        self.balance +=amount

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def __str__(self):
        print (f"{account_number:account_number}|{account_holder:account_holder}|{balance:balance}")
        
        
        
        
        
        
        
        
        


