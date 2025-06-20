from models.employee import Employee
from transactions.transaction_logger import TransactionLogger

class Manager(Employee):
    def __init__(self, emp_ID, name):
        super().__init__(emp_ID, name)
    
    def view_customer(self,customer):
        for c in customer:
            print(f"Customer ID: {c.cus_ID}, Name: {c.name}, Email: {c.email}")

    
    def m_view_logs(self):
        logs = TransactionLogger()
        logs.view_logs()