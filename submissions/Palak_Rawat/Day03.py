name=input("Enter your name: ")     #Taking user name using input() function
reverse=name[::-1]                  #Reversing the name given by user using slicing of string 
code=reverse.upper()                #Conerting the reverse name into uppercase using upper() function
#Now printing the final output , \n is used to go to new line
print(f"Original Name: {name}\nSecret Code: {code}")