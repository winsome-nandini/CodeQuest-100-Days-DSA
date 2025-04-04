# To print the sum of the digits of user input value

num=int(input("Enter a number: "))      # Here we are taking user input as integer 

string=str(num)                         # converting user input into string
s="0"                                   #Taking a string "s" to store the digits we are adding

for i in string:
    s=s+" + "+i                         # With the help of for loop we iterated every character of the string and stored them to "s"
#print(f"Value of s: {s}")

sum=0                                   # Here we are taking a variable "sum" assigned with value 0 so that we can store the actual sum in it
while num>0:                            # Using while loop till the number is greater than 0
    sum=(num%10)+sum                    # (num%10) will give the remainder and add it to the sum value
    num=num//10                         # Will give the Quotient and assign it to "num"
#print(string)
print(f"Sum of digits: {s[4:]} = {sum}")        # s[4:] will start the string from the actual number imput by user and printing 