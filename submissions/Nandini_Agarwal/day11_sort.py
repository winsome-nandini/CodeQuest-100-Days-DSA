n=input("Enter numbers: ")
#Taking numbers input

l=list(n)
#Changing string into list

for i in l:
    if i==" ":
        l.remove(i)
#Remove space from list

l.sort()
#Sorting list in ascending order

s=" ".join(l)
#Changing list into string

print("Sorted List:",s)