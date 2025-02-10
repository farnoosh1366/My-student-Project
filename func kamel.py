def kamel(n):
    b=[]
    for i in range(1,n):
      if n % i == 0:
           b.append(i)
    if sum (b) == n:
       return True
for j in range(1,10_001):
     if kamel(j)==True:
       print(j) 

