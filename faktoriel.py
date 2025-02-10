def factorial(n):
    if n == 0:
        return 1
    else:
        return n *factorial(n-1) 
n=int(input("Enter number="))
n1=int(input("Enter number="))
result = factorial(n)
result1= factorial(n1)
if  n-n1!=0:
    a=n-n1
    temp=factorial(a)
    r=result//(result1*temp)
print(r)