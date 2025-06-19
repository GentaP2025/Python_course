Banking final project

This project simulates a very basic banking system using Python. It allows users to manage customers, bank accounts, and transactions while providing functionality for logging and persisting data.

Package: models
Module: person - Create a person profile .
Class: Person which contain one method,  display info.
Initialization: Initializes a new person object with the provided name and email.
display_info method: The display_info method returns a formatted string with person details.
Module: Customer - Create and manage customer profiles.
Class: Customer , inherits from class Person and has one method, add_account.
Initialization: Initializes a new Customer object with the provided name, email, customer ID, and an optional list of bank accounts.
add_account method: Adds a bank account to the customer's list of accounts.
Module: employee - Create an employee profile.
Class : Employee
Initialization: Initializes a new person object with the provided employee ID and name. 
Module: manager - Admin capabilities to view customer information and logs.
Class: Manager , inherits from class Employee and has two methods, view_customer, m_view_logs.
view_customer method: Displays the details of the provided customers. Iterates through the list of customers and prints their details.
m_view_logs method: Displays transaction logs. This method should access the transaction log file and print its contents 

Package: accounts
Module: bank_accounts -Create bank accounts for customers, deposit and withdraw funds.
Class: BankAccount which contain three metods: deposi, withdraw, display_info .
Initialization: The constructor initializes the account number, account holder, and balance. 
Deposit Method: The deposit method correctly adds the specified amount to the balance.
Withdraw Method: The withdraw method checks if there are sufficient funds before deducting the amount. 
Display Info Method: The display_info method returns a formatted string with account details, which is used for displaying account information.

Package: transactions - Log all deposits and withdrawals.
Module: transaction logger
Class: TransactionLogger which contain four metods: log_transaction,log_customer,check_string_in_file,view_logs
log_customer method: Logs customer information to a CSV file. Opens the specified CSV file in append mode and writes the customer's details as a new row.
log_transaction: Logs a transaction (deposit or withdrawal) to a transaction log file. Opens the transaction log file in append mode and writes the transaction details.
check_string_in_file method: Checks if a string exists in a file. The method return "True" if the string id found , otherwise returs "False" and a message "String is not found id printed" . If the file does not exist or in case of any other error , the system through an respective exception message. 
view_logs methods: Read by blocks of data a file of logs and print the logs. If the file is empty , a message is thrown. 

Package: utils - Save and load customer data using JSON.
Module: file_handler , methods: save_customers, load_customers

save_customers : This function saves a list of Customer objects to a specified JSON file.
The with open(file_path, 'w') as file: line opens the specified file in write mode ('w'). If the file already exists, it will be overwritten. The json.dump function is used to serialize the list of customers into JSON format and write it to the file.
The list comprehension [customer.__dict__ for customer in customers] converts each Customer object into a dictionary. 

load_customers: This function loads customer data from a specified JSON file and returns a list of Customer objects.
The try block attempts to open the specified file in read mode ('r').json.load(file) reads the JSON data from the file and converts it back into Python objects (in this case, a list of dictionaries). The list comprehension [Customer(**data) for data in json.load(file)] creates a new Customer object for each dictionary in the loaded data. The **data syntax unpacks the dictionary, passing its keys as parameter names and values as parameter values to the Customer constructor.
If the file does not exist (raises a FileNotFoundError), the function returns an empty list [].

Folder: Data
Files: customer.csv - there are recorded the customr data
       transaction_log.txt - there are recorded the transaction details 
       customers.json - handle the serialization and deserialization of customer data to and from a JSON file

main module:
The main function is called when the script is executed.
First there are imported the necessary modules and classes. 
There are created two customers named Ana and Besi with an email and customer ID. These are objects of the Customer class.
It is checked if the customers already exists in the CSV file. If not, there are loged the customers' details.
For each customer there are created two accounts (objects of class BankAccount) and there are added to customer's account list.
For each account there are performed transactions by calling the methods of deposit and withdraw. 
Every transaction is logged in the transaction log text file. 
At the end , customer details and balance is printed on the screen. 

It is created a manager named Bob. It is an object of the Manager class.
He views the customer data and transaction logs by calling the methods of the Manager class 

At the end , it is saved a list of customers in a json file by calling the method "save_customer"  and after this there is a load of customers readed from a json file ("load_customer" method call) and converted into python objects, list of dictionaries. 


