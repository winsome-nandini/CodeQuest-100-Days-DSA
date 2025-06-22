s=input("Enter packet data: ")
cnt=0
for i in s:
    cnt+=ord(i)
check_sum=cnt%256
print("Check Sum: ",check_sum)