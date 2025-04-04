#include <stdio.h>
int main(){
    int num, sum=0, value;
    //Taking input from user
    printf("Enter the number ");
    scanf("%d", &num);

    while(num != 0){
        value = num % 10;// extracting last digit
        sum += value; //add it to sum
        num /= 10; //removing last digit
    }
       printf("Sum of digits : %d\n", sum);//printing the result
       return 0;
}