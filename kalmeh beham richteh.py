Text = input("Enter Your Text=")
Neutext=''
for c in Text:
 if (ord(c) >= ord("A") and ord (c) <= ord ("Z")) or (ord(c) <= ord("z") and ord(c) >= ord("a")):
    Neutext=Neutext+c
print(Neutext,end=" ")

