class TransactionLog ():

    def __init__(self):
        self.transactions = []

    def record(self,transaction):
        self.transactions.append(transaction)

    def get_all(self):
        return self.transactions
    

    def __str__(self):
        return  ("\n".join(f"- {t}" for t in self.transactions))


