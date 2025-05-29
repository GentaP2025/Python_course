class TransactionLog ():

    def __init__(self):
        self.transactions = {}

    def record(self, acc, transaction):
        if acc not in self.transactions:
            self.transactions[acc] = []  
        self.transactions[acc].append(transaction)
        

    def get_all(self, acc):
        return self.transactions[acc]
        
    

    def __str__(self):
        result = []
        for acc, trns in self.transactions.items():
            result.append(f"Account {acc}:")
            result.extend(f"  - {t}" for t in trns)
        return "\n".join(result)
