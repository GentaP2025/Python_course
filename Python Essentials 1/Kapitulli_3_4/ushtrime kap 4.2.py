#ushtrimi 1 

fjalor = {}

fjale = input("Shkruaj nje fjale: ")
for ch in fjale:
    if fjalor.keys !=ch:
        fjalor.update({ch:1})
print (fjale,"ka ", len(fjalor), "karaktere unike")

#****************************************************************
#usht 2

def removeOutliers(data, n):
    data_1 = sorted(data[:])
    if len(data_1) < 4:
        raise ValueError ("Duhet te shkruani me shume ne 4 karaktere")
    i = 1
    while i <= n:
       data_1.pop()
       data_1.pop(0)
       i += 1
    return data_1

def main():
    list1 = []
    list2 = []
    while True:
        vlera = input("Shkruaj nje vlere: ")
        if vlera == "":
            break
        list1.append(vlera)
    try: 
        list2 = removeOutliers(list1,2)
    except ValueError as error:
        print(error)

    print (list1,list2)
 
main()

#***********************************************************

#usht 3

def characterCounts(s):
    counts={}
    for ch in s:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return counts
    

def main():
    str1 = input("shkruaj fjalen e pare: ")
    str2 = input("shkruaj fjalen e dyte: ")
    if characterCounts(str1) == characterCounts(str2):
        print("Fjalet jane anagrame")
    else:
        print("Fjalet nuk jane anagrame")
        
main()