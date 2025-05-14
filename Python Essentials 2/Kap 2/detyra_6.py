#ush 1
def reverse_Lookup(d,value_find):
    list1=[]
    for key, value in d.items():
        if value_find == value:
            list1.append(key)
    return list1
    
def main():
    d = {"car":"makine", "dog":"qen", "apple":"molle","pencil":"laps","cap":"kapele","hat":"kapele"}
    
    print("Fjala anglisht per fjalen 'qen' eshte :" ,reverse_Lookup(d,"qen"))
    print("Fjala anglisht per fjalen 'mace' eshte :" ,reverse_Lookup(d,"mace"))
    print("Fjala anglisht per fjalen 'mace' eshte :" ,reverse_Lookup(d,"kapele"))
 
 
    
if __name__ == "__main__":
    main()

# ush 2 ********************************************************************************

tot = 0
while True:
    try:
        user_input = input("Input numbers: ")
        if user_input =="":
            break
        else:
            number = float(user_input)    
            tot +=number
            print("Total is: ",tot)
    except ValueError:
        print("This is not a number. Input a number")

# ush 3 ***********************************************************************************

def isInteg(fjale):
    fjale = fjale.strip()
    first_char = False
    isNumber = False
    i = 1 
    if ((fjale[0] == "+") or (fjale[0] == "-")) and len(fjale) > 1:
        first_char = True
    elif  fjale[0].isdigit(): 
        first_char = True
    
    if first_char == True:
        while i < len(fjale):
            if fjale[i].isdigit():
                i +=1
                isNumber = True
            else:
                isNumber = False
                break
    return isNumber

def main ():
    a = input("Input a string: ")
    if isInteg(a):
        print("String", a, "is integer")
    else:
        print("String", a, "is not integer")

if __name__ == "__main__":
    main()
