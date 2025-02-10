def Adad(n):
        h=0
        s=str(n)
        for i in s :
                if i=="2":
                   h=h+1           
        if h==2:
          return True
        else:
         return False
for j in range(1,10_001):
      if Adad (j)== True:
       print(j)
       