def Aval (n):
    t=[]
    for i in range(1,n+1):
        if n % i==0:
             t.append(i)
    if len(t)==2:
      return True
    else:
      return False 
s = 2
c = 0
n =int(input("Enter your number:"))
while c != n:
  if Aval(s)==True:
   c=c+1
   t = s
  s=s+1   
print(t)
 