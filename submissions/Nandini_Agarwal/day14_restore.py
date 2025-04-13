n=input("Enter string: ")
#Taking unfilled string input
l=[]

for i in range(ord(n[0]),ord(n[-1])+1):
#taking range from 1st charancter's ascii number to last character's ascii number+1 as range in loop doesn't count last value

    l.append(chr(i))
#changing ascii number into character and putting all characters in list

s="".join(l)
#Changing list into string

print("Restored string:",s)