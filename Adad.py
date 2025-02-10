def fard(n): 
    e=[]
    for i in range(1,n+1):
        if n % i == 0 and i%2==1 :
         e.append(i)
    return e
a=int(input("Enter your number="))
print(fard(a))