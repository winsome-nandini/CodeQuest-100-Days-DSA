lines = []
print("Alert List:")

while True:
    line = input()
    if not line: 
        break
    lines.append(line)
full_text = "\n".join(lines)

l=full_text.split("\n")
k=[]

for i in l:
    k.append(i.split())
for i in k:
    i.pop(0)
    i.remove("with")
    i.remove("priority")
    
d={}
for i in k:
    d[i[-1]]=" ".join(i[0:-1])
e=sorted(d)

print("Processing Alerts:")
for i in range(len(e)):
    print(f"{i+1}. {d.get(e[i])} (Priority: {e[i]})")