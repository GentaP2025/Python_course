#ush1
Pennies_per_nickel = 5

Nickel = 0.05
total = 0.00
total_pennies = 0.00
while True:
    price = input("Input price: ")
    if price =="":
        break
    total = total + float(price)
print("Total is :", round(total,2))
total_pennies = total * 100
if total_pennies % Pennies_per_nickel < 2.5:
    total_pennies = total_pennies - (total_pennies % Pennies_per_nickel)
else:
    total_pennies = total_pennies + Nickel - (total_pennies % Pennies_per_nickel)
    
cash_payment= round(total_pennies /100,2)
print(cash_payment)

***************************************************************************
#Ush 2 Password check:

def checkPassword(password):
    criter_1 = False
    criter_2 = False
    criter_3 = False
    criter_4 = False
    if len(password) >= 8:
        criter_1 = True
    for i in range (len(password)):
        if password[i].isupper():
            criter_2 = True
        elif   password[i].islower():
            criter_3 = True
        elif  password[i].isnumeric():
            criter_4 = True
    if   criter_1 == True and criter_2 == True and criter_3 == True and criter_4 == True:
        return "Good"
    else:
        return "Bad"
	
def main():
    P = input("Enter a password: ")
    print("The password is ", checkPassword (P))

main()

***************************************************************************
#ush 3 
l_neg=[]
l_poz=[]
l_0=[]
list_final =[]
while True:
    number = input("Input numbers: ")
    if number =="":
        break
    else:
        if int(number) < 0:
            l_neg.append(int(number))
        elif int(number) == 0:
             l_0.append(int(number))
        else:
             l_poz.append(int(number))
list_final = l_neg+l_0+l_poz
print(list_final)