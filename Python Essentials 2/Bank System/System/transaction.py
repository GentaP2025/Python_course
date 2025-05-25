class TransactionLog (self,transactions):

    def __init__(self):
        transactions = []

    def record(self,transaction):
        transactions.append(transaction)

    def get_all(self):
        return transactions
    

    def __str__(self):
        print(transactions.__dict__)


