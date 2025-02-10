
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result=1
for i in range(num2):
    result=result *num1
print(result)
def tavan(n,m):
    if m==1:#agar tavan1 n barmigardad
        return n
    else:
        return n*tavan(n,m-1)#vagarna maslan 2*2**3*2**2#har bbar yek vahed kam mishavad
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(tavan(num1,num2))









