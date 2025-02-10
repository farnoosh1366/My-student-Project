n= int(input("Enter Your Number ="))
for i in range(n):
    for j in range(n):
        if  j == 0  :
            print ("*",end="")
        elif i == j or  (i==n//2 and j<n-i):
            print("*", end ="")
        else: 
            print(" ", end ="")
    print()