#include<stdio.h>
void main()
{
    int n;
    printf("Enter the number\n");
    scanf("%d",&n);
    while(n%2==0)
    {
        n=n/2;
    }
     printf("%d\n",n);
}
