num=list(map(int, input("Enter numbers:").split()))
max_first=max_second=0
for i in num:
    if max_first < i:
        max_second=max_first
        max_first=i
    elif max_second < i & max_first != i:
        max_second =i
print("Second largest number: ",max_second)