from models.employee import Employee

class Manager(Employee):
    def __init__(self, emp_ID, name):
        super().__init__(emp_ID, name)
   

