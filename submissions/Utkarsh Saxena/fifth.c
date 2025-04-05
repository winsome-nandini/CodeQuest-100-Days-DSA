#include <stdio.h>
int main(){
    int N;

    printf("Enter a number");//taking input from user
    scanf("%d", &N);
     for(int i=1;i<=N;i++){  //loop from 1 to N
        printf("%d\n",i);
     }
     return 0;
}