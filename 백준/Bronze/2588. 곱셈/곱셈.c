#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int A,B ;
    scanf("%d",&A);
    scanf("%d", &B);

    printf("%d\n", A*(B%10));
    printf("%d\n", A*(B/10%10));
    printf("%d\n", A*(B/100));
    printf("%d", (A *(B % 10))+( A * (B / 10 % 10))*10 + A * (B / 100)*100);
   

 

    return 0;
}
