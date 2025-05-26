class TransactionLog ():

    def __init__(self):
        transactions = []

    def record(self,transaction):
        self.transactions.append(transaction)

    def get_all(self):
        return self.transactions
    

    def __str__(self):
        print(self.transactions.__dict__)


