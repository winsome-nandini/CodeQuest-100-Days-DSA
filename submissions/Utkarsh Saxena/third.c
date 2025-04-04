#include <stdio.h>
#include <ctype.h>
#include <string.h>
int main(){
    char name[200];
    printf("Enter your name: ");
    scanf("%s", name);
printf("Original Name: %s\n", name);
    int l = strlen(name);
    printf("Secret Code: ");
    for(int i= l-1; i>=0; i--){
        printf("%c",toupper(name[i]));
    }
    return 0;
}