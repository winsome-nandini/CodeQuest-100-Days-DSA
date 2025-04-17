n=int(input("Enter the number of terms: "))
#taking input of numbers
l=[0,1]

print("Fibonacci sequence:",end=" ")

for i in range(n):
    print(l[-2],end=" ")
    l.append(l[-2]+l[-1])