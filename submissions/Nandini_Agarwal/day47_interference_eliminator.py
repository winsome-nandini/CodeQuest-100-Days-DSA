l1=list(map(int,input("Enter signal (space-separated): ").split()))
w=int(input("Enter window size (W):"))
l2=[]
for i in range(len(l1)-(w-1)):
    s=0
    for j in range(w):
        s+=l1[i+j]
    l2.append(int(s/w))
print("Smoothed Signal:"," ".join(map(str,l2)))