def Aval (n):
    t=[]
    for i in range(1,n+1):
        if n % i==0:
             t.append(i)
    if len(t)==2:
      return True
    else:
      return False
def tamamAval(n):
    flag = True
    while n!=0:
        if Aval(n)==False:
            flag = False
        n=n//10
    if flag == True:
        return True
    else:
        return False
a=10000
for i in  range(2,a):
  if tamamAval(i)==True:
   print(i)
