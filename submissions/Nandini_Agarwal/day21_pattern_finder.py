def sum_even_position_num(array):
    count=0
    for i in range(len(array)):
        if i%2!=0:
            count += int(array[i])
    return count

array=input("Enter elements separated by space:").split()
print("Hidden Key:", sum_even_position_num(array))