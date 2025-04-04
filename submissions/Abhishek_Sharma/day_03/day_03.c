#include<stdio.h>
#include <ctype.h>
#include<string.h>
void reverseString(char* str) {
    int len = 0;
    while (str[len] != '\0') len++;
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

int main() {
    char str[100];

    // Take first input (stops at space)
    printf("Enter your name: ");
    scanf("%s", str);
    char str1[100];
    strcpy(str1, str);
    printf("Uppercase name by inbuilt: %s\n",toupper(str1[100]));  // Converts to uppercase
    // Convert to uppercase
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - ('a' - 'A');
        }
    }
    printf("Uppercase name: %s\n", str);

    // Reverse the string
    reverseString(str);
    printf("Reversed name: %s\n", str);

    // Clear leftover '\n' from scanf
    getchar();

    // Take full line input (including spaces)
    printf("Enter another string: ");
    fgets(str, sizeof(str), stdin);
    printf("You entered: %s", str);

    return 0;
}