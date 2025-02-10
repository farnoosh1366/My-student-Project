A=['A','D','A','A','A','A','A','B','D','A','C','A','A','A','C','A','B','B','D','B']
mylist = []
for i in range(20):
    user = input(f"Enter a letter for index :{i}:A,B,C,D: ")
    mylist.append(user)
T=0
for A,mylist in zip(A,mylist):
    if mylist==A:
        T=T+1
print("List right:",T)