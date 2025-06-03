from models.person import Person
    
class Customer(Person):
    def __init__(self, name, email, balance=0):
        super().__init__(name, email)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New Balance: {self.balance}"
        else:
            return "Insufficient funds."
