n=input("Enter numbers: ")
#taking input of numbers

l=list(n)
#Putting all numbers in a single list

s=0
#Initially the sum is 0

for i in l:
#Taking each element from list
    if i!=" ":
    #Ignoring " " and taking numbers
        s+=int(i)
        #Changing number from string to integers and adding them in sum 

print("Secret Code:",s)