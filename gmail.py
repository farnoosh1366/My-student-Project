Mail=input("Enter Email:")
n = ["@","gmail",".com"]
a=0
for f in Mail:
    if f  in n:
      a = 1
if a==1:
    print("Yes")

else:
    print ("No")    