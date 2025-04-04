#include<stdio.h>
int main(){
char str[100];
printf("Enter your name:");
scanf("%s",str);
// Convert the string to uppercase
for (int i = 0; str[i] != '\0'; i++) {
    if (str[i] >= 'a' && str[i] <= 'z') {
        str[i] = str[i] - ('a' - 'A');
    }
}
printf("Uppercase name: %s\n", str);
// Function to reverse a string
void reverseString(char* str) {
    int len = 0;
    while (str[len] != '\0') len++;
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

// Reverse the string
reverseString(str);
printf("Reversed name: %s\n",str);
fgets(str, sizeof(str), stdin);  // Reads until newline or buffer is full
printf("You entered: %s", str);
//scanf(" %[^\n]", str);  // The space before % consumes any leftover newline
printf("You entered: %s\n", str);
    return 0;
}