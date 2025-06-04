l=list(map(int,input("Enter frequencies (space-separated): ").split()))
max_count=l[0]
for i in l:
    if l.count(i)>l.count(max_count):
        max_count= i
c=l.count(max_count)
print(f"Most common frequency: {max_count} ( occur {c} times)")