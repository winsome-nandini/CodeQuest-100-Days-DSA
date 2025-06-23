arr = input("Enter intervals (format: start-end, space-separated): ").split()
b=sorted(arr)
l=[]
for i in b:
    l.append(i.split("-"))
l1=[]
for i in range(1,len(l)):
    if i ==1:
        l1.append([l[i-1][0],l[i][1]])
    else:
        l1.append(l[i])
print(l1)