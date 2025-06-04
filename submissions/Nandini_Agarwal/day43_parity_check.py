def binary_count(s):
    count=0
    for i in s:
        if i=="1":
            count+=1
    if count%2==0:
        return "Even Parity"
    else:
        return "Odd Parity"
binary=input("Enter binary signal: ")
print(binary_count(binary))