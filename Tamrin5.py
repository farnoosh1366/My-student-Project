n = input("enter your password =")
p = 0
a = 0
b = 0
c = 0
sp = ["~","!","@","#","$","%","^","&","*","(",")","_","-","+","="]
cod= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ["1","2","3","4","5","6","7","8","9","10"]
if len(n) >= 8:
    p = 1
for f in n:
    if f  in sp:
     a = 1
for g in n:
    if g in cod:
     b = 1
for h in n:
    if h in numbers:
        c = 1
if a == 1 and b == 1 and c ==1 and p ==1: 
    print ("amn")
  
else:
    print("na amn")
    
