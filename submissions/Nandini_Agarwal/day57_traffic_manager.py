arr = list(map(int,input("Initial Traffic Data: ").split()))
no_query=int(input("Number of queries:"))
l=[]
for i in range(no_query):
    b=input(f"Query {i+1}:").split()
    l.append(b)

for i in l:
    if i[0]=="Query":
        print(f"Prefix sum (index {i[-1]}):", end=" ")
        s=0
        sub = arr[0:int(i[-1])]
        for j in range(arr[int(i[-1])]):
            s+=j
        print(" + ".join(map(str,sub)),"=",s)
 
    elif i[0]=="Update":
        arr[int(i[2])]+=int(i[5])