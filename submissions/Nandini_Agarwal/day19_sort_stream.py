
n=input("Enter numbers: ")
l=list(n)
for i in l:
    if i.isdigit()==False:
        l.remove(i)
        
s=l.sort()

print("Sorted: "," ".join(l))