n1=float(input("Enter number 1:"))
n2=float(input("Enter number 2:"))
n3=float(input("Enter number 3:"))
if n1>=n2 and n2>=n3:
    print("Max =",n1)
elif n2>=n1 and n1>=n3:
    print("Max =",n2)
elif n3>=n1 and  n1>=n2:
    print("Max =",n3)    
    

