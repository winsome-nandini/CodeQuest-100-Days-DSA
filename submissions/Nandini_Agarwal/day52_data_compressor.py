s = input("Enter data packet: ")
l = []

group = s[0]  

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        group += s[i]
    else:
        l.append(group)
        group = s[i]

l.append(group) 

print("Compressed Data:")
for i in l:
    print(f"{len(i)}{i[0]}",end="")