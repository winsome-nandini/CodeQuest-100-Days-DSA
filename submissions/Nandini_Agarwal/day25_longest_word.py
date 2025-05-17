n=input("Enter a sentence: ").split()
l=n[0]
for i in n:
    if len(i)>len(l):
        l=i
print("Longest word:",l)