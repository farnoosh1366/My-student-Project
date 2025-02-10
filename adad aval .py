def aval (n):
    t=[]
    for i in range(1,n+1):
        if n % i==0:
             t.append(i)
    if len(t)==2:
      return True
    else:
      return False
a=int(input("Enter number="))
b=int(input("Enter number="))
c=[]
for j in range(a,b+1):
     if aval (j) == True:
         c.append(j)
print(len(c))
    

