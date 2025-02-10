import random
Mynumber =int(input("Enter your number="))
while True:
   number=random.randint(1,100)
   if number>Mynumber:
    print("My number is big")
   if number<Mynumber:
    print("My number is smal")
   if number==Mynumber:
     print("True",number)
     break