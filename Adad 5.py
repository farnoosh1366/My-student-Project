def  zuj (n1):
      s =str(n1)
      a=[]
      for i in s:
       if int(i)%2==0:
         a.append(int(i))
      return sum(a)
def  fard (n2):
      b =str(n2)
      c=[]
      for j in b:
       if int(j)%2!=0:
        c.append(int(j))
      return sum(c)
for a in range(1,10000):
   if zuj(a) == fard(a):
    print(a)
    

