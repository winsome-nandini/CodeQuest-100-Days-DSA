n=int(input("Enter a number: "))
#Taking input of number

f=1
#Initially the factorial is 1

for i in range(1,n+1):
#Multiplying each number from 1 to n, as loop doesn't count the stop value
    f*=i

print("Factorial of",n,"is",f)