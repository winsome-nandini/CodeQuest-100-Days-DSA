n=input("Enter sentence: ")
vowel=0
Consonent=0
for i in n:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U" :
        vowel+=1 
    else:
        Consonent+=1
print("Vowels:",vowel,"\nConsonents:",Consonent)