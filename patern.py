n= 11
for j in range(n):
    for i in range(n):
        if   i == j  :
            print ("*",end="")
        elif i<=n//2 and  j+i==n-1 :
            print("*", end = "")
        else: 
            print(" ", end ="")
    print()