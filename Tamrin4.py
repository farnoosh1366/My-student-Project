n = input("enter your password =")
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
newWord = ''
for i in n:
      newWord =newWord + c[(ord(i)+3-97)%26]
print(newWord)
