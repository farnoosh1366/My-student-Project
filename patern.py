n=int(input("Enter namber ="))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==0 or j==n-1 :
            print ("*",end=" ")
        else: 
            print(" ", end = " ")
    print()
       