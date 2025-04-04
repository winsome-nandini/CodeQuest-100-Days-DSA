num = str(input("Enter the number: "))
sum = 0
digit_details = ""

for i in range(len(num)):
    sum += int(num[i])
    digit_details += num[i]
    if i != len(num) - 1: 
        digit_details += " + "

print(f"Sum of digits: {digit_details} = {sum}")
