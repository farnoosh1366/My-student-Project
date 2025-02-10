a = input("Enter your Num positiv and 3raghami=")
b = input("Enter your Num positiv and 3raghami=")
num1 = list(a)
num1.reverse()
num2 = list(b)
num2.reverse()
if num1< num2:
    print(a, "<", b)
elif num2 < num1:
    print(b, "<", a)
else:
    print(a, "=", b)