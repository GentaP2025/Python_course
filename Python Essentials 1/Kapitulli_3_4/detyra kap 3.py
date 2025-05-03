#ush1
string = input("Write a word: ")
string = string.upper()

palindrome = True  

i = 0
while i < len(string) // 2:
    if string[i] != string[len(string) - i - 1]:
        palindrome = False
        break
    i += 1

if palindrome:
    print("String", string, "is a palindrome")
else:
    print("String", string, "is not a palindrome")
	
#*************************************************
#ush2

n = int(input("Enter first  number:  "))
m = int(input("Enter second  number:  "))
d = min(n,m)
while d >1:
    if n % d == 0 and m % d == 0:
        print(d," is the greatest common divisor")
        break
    else:
        d-=1
#**************************************************
#ush 3

a = int(input("Enter room length:  "))
b = int(input("Enter room width:  "))

area = a*b

print("The area of the room is ",area)

#***********************************************

#ush 4

Baby_Cost = 0
Child_Cost = 14
Senior_Cost = 18
Adult_Cost = 23

Baby_Limit = 2
Child_Limit = 12
Adult_Limit = 64

tot_cost = 0

while True:
    age = input("Enter guest age: ")
    if age =="":
        break
    else:
        age = int(age)
    if age <= Baby_Limit:
        tot_cost = tot_cost + Baby_Cost
    elif age <= Child_Limit:
        tot_cost = tot_cost + Child_Cost
    elif  age >= Adult_Limit:
        tot_cost = tot_cost + Senior_Cost
    else:
        tot_cost = tot_cost + Adult_Cost
print("Total cost is ",float(tot_cost),"$")

#********************************************
#ush 5

list1=[]
i=0
while True:
    word = input("Enter a word: ")
    if word =="":
        break
    else:
       if word not in list1:
           list1.append(word) 
           i+=1
print(list1)

