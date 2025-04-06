#include <stdio.h>
#include <string.h>
int main(){
    char choice[100];
    printf("Which path do you choose (left or right)");
    scanf("%s", choice);

    if(strcmp(choice, "right")== 0){
        printf("Oh no!, The Glitch's trap was here! Try again.\n");
    }else if(strcmp(choice, "left")==0){
        printf("You found a hidden tunnel! You're Safe \n");
    }else{
        printf("Invalid choice. Please Entetr 'left' or 'right'. \n");
    }
    return 0;
}