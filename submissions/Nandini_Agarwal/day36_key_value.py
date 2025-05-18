a=input("").split()
b={}
for i in a:
    b[i]=a.count(i)
print("Current Stack: ",b)