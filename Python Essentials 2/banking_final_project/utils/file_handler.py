import json
from  models.customer import Customer

def save_customers(customers, file_path):
    with open(file_path, 'w') as file:
        json.dump([customer.__dict__ for customer in customers], file)

def load_customers(file_path):
    try:
        with open(file_path, 'r') as file:
            return [Customer(**data) for data in json.load(file)]
    except FileNotFoundError:
        return []