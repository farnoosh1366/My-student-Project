def donbale(n):
    if n == 0:
        return 1
    else:
      return  n*n / ((2*n-1)+1)
n=int(input("Inter your Number="))
res = 0
for i in range(1,n+1):
    r=donbale(i)
    res=res+r
print(res)
