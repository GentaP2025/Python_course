from models.person import Person

class Customer(Person):    
    def __init__(self, name, email, cus_ID, bank_acc=None):
        super().__init__(name, email)
        self.cus_ID = cus_ID
        self.bank_acc = bank_acc if bank_acc is not None else []

    def add_account(self,account):
        self.bank_acc.append(account)
       