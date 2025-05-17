n=input("Enter binary number:")[::-1]
count=0
for i in range(len(n)):
    count+=(int(n[i])*(2**i))
print("Decimal:",count)