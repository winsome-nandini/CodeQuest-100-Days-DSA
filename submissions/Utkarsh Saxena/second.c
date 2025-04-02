#include <stdio.h>
int main(){
    char name[300];
    printf("Hello,Cyberpunk city!\n");
    printf("What is your name?\n");// \n used to skip to next line
    scanf("%299s", name);// read user input but with a limit to avoid overflow
    printf("Welcome to the adventure, %s!", name);
    return 0;
}