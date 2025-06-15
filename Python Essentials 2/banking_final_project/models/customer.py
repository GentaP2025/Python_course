from models.person import Person

class Customer(Person):    
    def __init__(self,name,email,cus_ID,bank_acc):
        super().__init__(name, email)
        self.cus_ID = cus_ID
        self.bank_acc = bank_acc
       