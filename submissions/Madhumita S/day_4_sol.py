a=input('Enter a number: ')
print('Sum of digits: ',end='')
sum=0
for i in range(0,len(a)): 
    sum+=int(a[i])
    print(a[i],end=' + ') if(i!=len(a)-1) else print(a[i],end=' = ')
print(sum)