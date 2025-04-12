n=input("Enter N: ")
#Taking number input
l=[]
#Taking Empty List to store even numbers

for i in n:
    if int(i)%2==0:
        l.append(i)
        #Storing even numbers in List l
        
if len(l)==0:
    print("No even digits found!")
    #If there is no even number
    
else:
    s=" ".join(l)
    #Changing list into string

    print("Even digits:",s)