#include<stdio.h>
#include<string.h>
int main(){
    char choice[100];
    printf("Which path do you choose (left/right)");//taking input from user
    scanf("%s", choice);

    if(strcmp(choice, "left")==0){//comapring input with 'left'
        printf("You found a hidden Tunnel! You're Safe. ");
    }else if(strcmp(choice, "right")==0){//comparing input with 'right'
        printf("Oh no! The Glitch's trap was here! Try Again. ");
    }else{ //case of failure
        printf("Ivalid Choice.Please enter 'left' or 'right'");

    }
    return 0;
}