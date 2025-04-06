#sum of digits
def sum_of_dig(n):
    return sum(int(digit) for digit in (str(abs(n))))
    
n=int(input("Enter the number: "))
print("The sum of Password is :",sum_of_dig(n))




#Enter the number: 98765
#The sum of Password is : 35