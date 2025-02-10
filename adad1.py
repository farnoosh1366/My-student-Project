r =1000
b = []
for item in range(1,r):
    if item % 6 == 0 and item%9!=0:
      b.append(item)
b=sum(b)
print(b)