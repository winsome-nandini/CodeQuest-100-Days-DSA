n=input("Enter module scores (space-separated): ").split()
l=[]
for i in n:
    if int(i)<50 :
        l.append(i)
if len(l)>=1:
    print("Modules to debug:"," ".join(l))
else:
    print("All modules are working fine!")