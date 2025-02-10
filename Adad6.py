def Aval (n):
    t=[]
    for i in range(1,n+1):
        if n % i==0:
             t.append(i)
    if len(t)==2:
      return True
    else:
      return False 
def majmo(a):
    u = []
    s = str(a)
    for i in s:
        u.append(int(i))
    return sum(u)   
n=1000
for c in range(2,n):
    if Aval(c)==True and Aval(majmo(c))==True:
        print(c)


